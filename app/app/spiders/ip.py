# -*- coding: utf-8 -*-
import scrapy


class IpSpider(scrapy.Spider):
    """
    IP代理测试 蜘蛛
    使用：
    进入项目目录
    $ scrapy crawl ip
    """
    name = "ip"
    allowed_domains = ["ip.cn"]
    start_urls = (
        'http://ip.cn/index.php',
    )

    def parse(self, response):
        info = response.xpath('//div[@class="well"]//code/text()').extract()
        ip_info = dict(zip(['ip', 'address'], info))
        yield ip_info
