#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: middlewares.py
@time: 16-2-24 上午11:23
"""


import random
import hashlib
import redis
from scrapy.exceptions import IgnoreRequest


class UserAgentMiddleware(object):
    """
    Randomly rotate user agents based on a list of predefined ones
    """
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class HttpProxyMiddleware(object):
    """
    随机选择代理
    """
    def __init__(self, proxy_list):
        self.proxy_list = proxy_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('PROXY_LIST'))

    def process_request(self, request, spider):
        # Set the location of the proxy
        # request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
        # request.meta['proxy'] = "http://125.122.140.27:18186"
        # IP地址：[125.122.140.27] 浙江省杭州市 电信
        # request.meta['proxy'] = "http://106.81.213.207:8080"
        request.meta['proxy'] = random.choice(self.proxy_list)


class IgnoreRequestMiddleware(object):
    """
    url 请求去重
    """
    def __init__(self, redis_host, redis_port):
        self.redis_client = redis.Redis(host=redis_host, port=redis_port)

    @classmethod
    def from_crawler(cls, crawler):
        redis_config = crawler.settings.get('REDIS')
        return cls(
            redis_host=redis_config.get('host', 'localhost'),
            redis_port=redis_config.get('port', 6379)
        )

    def process_request(self, request, spider):
        if not request.url:
            return None
        url_hash = hashlib.md5(request.url.encode("utf8")).hexdigest()
        if self.redis_client.sismember(spider.name, url_hash):
            raise IgnoreRequest("Spider : %s, IgnoreRequest : %s" % (spider.name, request.url))
        else:
            self.redis_client.sadd(spider.name, url_hash)


class ContentTypeGb2312Middleware(object):
    """
    处理不规范的页面（优先级降低至580之后才能生效）
    指定 Content-Type 为 gb2312
    """
    def process_response(self, request, response, spider):
        response.headers['Content-Type'] = 'text/html; charset=gb2312'
        return response
