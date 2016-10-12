# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from ..models.v4 import ServiceV4
from ..items.v4 import ServiceV4Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
            sqlalchemy_pool_size=crawler.settings.get('SQLALCHEMY_POOL_SIZE', 8)
        )

    def open_spider(self, spider):
        self.session = self.db_session()

    def process_item(self, item, spider):
        try:
            if isinstance(item, ServiceV4Item):
                service_item = ServiceV4(**item)
                self.session.add(service_item)
                self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item

    def close_spider(self, spider):
        self.session.close()
