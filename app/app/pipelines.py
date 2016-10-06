# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
import scrapy
import hashlib
import json
import redis
from urllib import quote
from scrapy.exceptions import DropItem
from models import Company, Position
from items import CompanyItem, PositionItem
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
    (Base Redis)
    """
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            url_hash = hashlib.md5(item['detail_url'].encode("utf8")).hexdigest()
            if self.redis_client.exists('url:%s' % url_hash):
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.redis_client.set('url:%s' % url_hash, 1)
        return item


class JsonWriterPipeline(object):
    """
    The purpose of JsonWriterPipeline is just to introduce how to write item pipelines.
    If you really want to store all scraped items into a JSON file you should use the Feed exports.
    """
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class StoreMongoDBPipeline(object):
    """
    基于 MongoDB 的存储
    """
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item


class StoreMySQLPipeline(object):
    """
    基于 MySQL 的存储
    """
    def __init__(self, sqlalchemy_database_uri, sqlalchemy_pool_size):
        self.engine = create_engine(sqlalchemy_database_uri, pool_size=sqlalchemy_pool_size)
        self.db_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sqlalchemy_database_uri=crawler.settings.get('SQLALCHEMY_DATABASE_URI_MYSQL'),
            sqlalchemy_pool_size=crawler.settings.get('SQLALCHEMY_POOL_SIZE', 5)
        )

    def open_spider(self, spider):
        self.session = self.db_session()

    def process_item(self, item, spider):
        try:
            if isinstance(item, CompanyItem):
                company_item = Company(**item)
                self.session.add(company_item)
                self.session.commit()
            if isinstance(item, PositionItem):
                position_item = Position(**item)
                self.session.add(position_item)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def close_spider(self, spider):
        self.session.close()


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
            if isinstance(item, CompanyItem):
                company_item = Company(**item)
                self.session.add(company_item)
                self.session.commit()
            if isinstance(item, PositionItem):
                position_item = Position(**item)
                self.session.add(position_item)
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
