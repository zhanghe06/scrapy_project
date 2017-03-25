# -*- coding: utf-8 -*-
import scrapy
import json
import time


class IpCnSpider(scrapy.Spider):
    name = "ip_cn"
    allowed_domains = ["ip.cn"]
    # start_urls = ['http://ip.cn/']
    start_urls = (
        'http://ip.cn/index.php?k=1',
        'http://ip.cn/index.php?k=2',
        'http://ip.cn/index.php?k=3',
        'http://ip.cn/index.php?k=4',
    )
    custom_settings = dict(
        COOKIES_ENABLED=True,
        DOWNLOAD_DELAY=2,
        CONCURRENT_REQUESTS_PER_DOMAIN=1,
        CONCURRENT_REQUESTS_PER_IP=1,
        DOWNLOADER_MIDDLEWARES={'app.middlewares.IgnoreRequestMiddleware': None}
    )

    def parse(self, response):
        info = response.xpath('//div[@class="well"]//code/text()').extract()
        ip_info = dict(zip(['ip', 'address'], info))
        ip_info['fetch_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
        ip_info['s'] = response.meta.get('s', '')
        ip_info['cookiejar'] = response.meta.get('cookiejar', '')
        print json.dumps(ip_info, indent=4, ensure_ascii=False)
        yield ip_info


"""
{
    "ip": "101.81.81.10",
    "fetch_time": "2017-01-09 18:30:58",
    "address": "上海市 电信"
}
{
    "ip": "101.81.81.10",
    "fetch_time": "2017-01-09 18:31:12",
    "address": "上海市 电信"
}
{
    "ip": "101.81.81.10",
    "fetch_time": "2017-01-09 18:31:27",
    "address": "上海市 电信"
}
{
    "ip": "101.81.81.10",
    "fetch_time": "2017-01-09 18:31:38",
    "address": "上海市 电信"
}
"""


"""
✗ scrapy crawl ip_cn
✗ curl http://localhost:6800/schedule.json -d project=default -d spider=ip_cn -d setting=DOWNLOAD_DELAY=10
"""
