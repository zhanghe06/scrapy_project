# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    site = scrapy.Field()
    address = scrapy.Field()
    industry = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()


class PositionItem(scrapy.Item):
    title = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    industry = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    description = scrapy.Field()
    detail_url = scrapy.Field()
    list_url = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
