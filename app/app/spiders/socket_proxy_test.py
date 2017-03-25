# -*- coding: utf-8 -*-
import scrapy


class SocketProxyTestSpider(scrapy.Spider):
    name = "socket_proxy_test"
    allowed_domains = ["ip.cn"]
    start_urls = (
        'http://ip.cn',
    )

    custom_settings = dict(
        DOWNLOADER_MIDDLEWARES={
            'app.middlewares.HttpProxyMiddleware': 120
        },
        PROXY_LIST=['http://127.0.0.1:8118']  # socks 转 http
        # PROXY_LIST=['socks5://127.0.0.1:1080']  # 不支持
    )

    def parse(self, response):
        info = response.xpath('//div[@class="well"]//code/text()').extract()
        ip_info = dict(zip(['ip', 'address'], info))
        yield ip_info


"""
✗ scrapy genspider socket_proxy_test ip.cn
✗ scrapy crawl socket_proxy_test
"""
