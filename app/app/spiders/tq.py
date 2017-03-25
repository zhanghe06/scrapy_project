# -*- coding: utf-8 -*-
import scrapy


class WeatherSpider(scrapy.Spider):
    """
    页面不规范，Content-Type 没有指定 charset
    """
    name = "tianqihoubao"
    allowed_domains = ["tianqihoubao.com"]
    start_urls = [
        "http://www.tianqihoubao.com/lishi/"
    ]
    custom_settings = dict(
        DOWNLOADER_MIDDLEWARES={
            'app.middlewares.ContentTypeGb2312Middleware': 585,  # 优先级降低至580之后才能生效
        }
    )

    def parse(self, response):
        print response.body_as_unicode()
        print response.encoding
