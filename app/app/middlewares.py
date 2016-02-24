#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: middlewares.py
@time: 16-2-24 上午11:23
"""


class HttpProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        # request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
        # request.meta['proxy'] = "http://125.122.140.27:18186"
        # IP地址：[125.122.140.27] 浙江省杭州市 电信
        request.meta['proxy'] = "http://106.81.213.207:8080"
