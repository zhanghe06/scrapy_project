#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: stats.py
@time: 2017/5/9 上午11:00
"""


from scrapy import signals
import time


class StatsPipeline(object):
    """
    app.pipelines.stats.StatsPipeline
    """
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)  # 关闭蜘蛛（释放蜘蛛资源）
        return pipeline

    def close_spider(self, spider):
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'StatsPipeline   Process: close_spider'
        print spider.crawler.stats.get_stats()

    def spider_closed(self, spider, reason):
        """
        关闭蜘蛛（释放蜘蛛资源）
        :param spider:
        :param reason: finished/cancelled/shutdown
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'StatsPipeline   Signals: spider_closed'
        print spider.crawler.stats.get_stats()
        print spider.crawler.stats.get_value('downloader/request_count', 0)  # 请求数量
        print spider.crawler.stats.get_value('downloader/response_count', 0)  # 响应数量
        print spider.crawler.stats.get_value('response_received_count', 0)  # 响应接收数量
        print spider.crawler.stats.get_value('item_dropped_count', 0)  # 丢弃数据数量
        print spider.crawler.stats.get_value('item_scraped_count', 0)  # 有效数据数量
