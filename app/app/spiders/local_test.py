# -*- coding: utf-8 -*-
import scrapy


class LocalTestSpider(scrapy.Spider):
    name = "local_test"
    allowed_domains = ["localhost:8000"]
    start_urls = (
        'http://localhost:8000/blog/list/',
    )

    def parse(self, response):
        for name in response.xpath('//tr/td[3]/text()').extract():
            print '-'*8, name
            yield {'name': name}
