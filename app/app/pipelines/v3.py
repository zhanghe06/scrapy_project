# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy
import hashlib
import redis
from urllib import quote
from scrapy.exceptions import DropItem
from ..models.v3 import OriginProviderV3, OriginServiceV3
from ..items.v3 import ProviderV3Item, ServiceV3Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class AppPipeline(object):
    def process_item(self, item, spider):
        return item


class DuplicatesMemoryPipeline(object):
    """
    A filter that looks for duplicate items, and drops those items that were already processed.
    (Base Memory)
    """
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item


class DuplicatesRedisPipeline(object):
    """
    # service
    # (source_type, title)
    #
    # provider
    # (full_name, source_type)
    (Base Redis)
    """
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def process_item(self, item, spider):
        if isinstance(item, ProviderV3Item):
            key = item['full_name'].encode('utf-8') + str(item['source_type'])
            url_hash = hashlib.md5(key).hexdigest()
            if self.redis_client.exists('p:%s' % url_hash):
                self.redis_client.incr('p:%s' % url_hash, 1)
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.redis_client.set('p:%s' % url_hash, 1)
        if isinstance(item, ServiceV3Item):
            key = str(item['source_type']) + item['title'].encode('utf-8')
            url_hash = hashlib.md5(key).hexdigest()
            if self.redis_client.exists('s:%s' % url_hash):
                self.redis_client.incr('s:%s' % url_hash, 1)
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.redis_client.set('s:%s' % url_hash, 1)
        return item


class StorePostgreSQLPipeline(object):
    """
    基于 PostgreSQL 的存储
    """
    def __init__(self, sqlalchemy_database_uri, sqlalchemy_pool_size):
        self.engine = create_engine(sqlalchemy_database_uri, pool_size=sqlalchemy_pool_size)
        self.db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlalchemy_database_uri=crawler.settings.get('SQLALCHEMY_DATABASE_URI_PG'),
            sqlalchemy_pool_size=crawler.settings.get('SQLALCHEMY_POOL_SIZE', 5)
        )

    def open_spider(self, spider):
        self.session = self.db_session()

    def process_item(self, item, spider):
        try:
            if isinstance(item, ProviderV3Item):
                provider_item = OriginProviderV3(**item)
                self.session.add(provider_item)
                self.session.commit()
            if isinstance(item, ServiceV3Item):
                service_item = OriginServiceV3(**item)
                self.session.add(service_item)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def close_spider(self, spider):
        self.session.close()


class ScreenshotPipeline(object):
    """
    Pipeline that uses Splash to render screenshot of every Scrapy item.
    """
    SPLASH_URL = "http://localhost:8050/render.png?url={}"

    def process_item(self, item, spider):
        encoded_item_url = quote(item["url"])
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screenshot_url)
        dfd = spider.crawler.engine.download(request, spider)
        dfd.addBoth(self.return_item, item)
        return dfd

    def return_item(self, response, item):
        if response.status != 200:
            # Error happened, return item.
            return item

        # Save screenshot to file, filename will be hash of url.
        url = item["url"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        filename = "{}.png".format(url_hash)
        with open(filename, "wb") as f:
            f.write(response.body)

        # Store filename in item.
        item["screenshot_filename"] = filename
        return item
