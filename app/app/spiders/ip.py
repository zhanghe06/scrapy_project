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
        ip_list = response.xpath('//div[@id="result"]/div/p[1]/code/text()').extract()
        ip_address_list = response.xpath('//div[@id="result"]/div/p[1]/text()').extract()
        if ip_list:
            ip = ip_list[0]
            ip_address = ip_address_list[1].lstrip(u' 来自：')
            print u'IP地址：[%s] %s' % (ip, ip_address)
            yield {'ip': ip, 'ip_address': ip_address}
        else:
            print u'IP地址获取失败'
