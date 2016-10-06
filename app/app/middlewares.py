#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: middlewares.py
@time: 16-2-24 上午11:23
"""
import random


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
