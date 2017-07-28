#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: signals.py
@time: 2017/4/28 下午2:43
"""


from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter
import time
from random import randint


class SignalsPipeline(object):
    """
    app.pipelines.exporter_signals.SignalsPipeline
    专有方法：
        process_item
    """
    def __init__(self):
        self.files = {}
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.engine_started, signals.engine_started)  # 引擎启动
        crawler.signals.connect(pipeline.engine_stopped, signals.engine_stopped)  # 引擎停止
        crawler.signals.connect(pipeline.item_scraped, signals.item_scraped)  # 数据保留（通过管道）
        crawler.signals.connect(pipeline.item_dropped, signals.item_dropped)  # 数据丢弃（移出管道）
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)  # 打开蜘蛛（保留蜘蛛资源）
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)  # 关闭蜘蛛（释放蜘蛛资源）
        crawler.signals.connect(pipeline.spider_idle, signals.spider_idle)      # 蜘蛛空闲
        crawler.signals.connect(pipeline.spider_error, signals.spider_error)    # 蜘蛛错误
        crawler.signals.connect(pipeline.request_scheduled, signals.request_scheduled)    # 引擎调度请求
        crawler.signals.connect(pipeline.request_dropped, signals.request_dropped)    # 引擎放弃请求
        crawler.signals.connect(pipeline.response_received, signals.response_received)    # 接收响应
        crawler.signals.connect(pipeline.response_downloaded, signals.response_downloaded)    # 下载响应
        return pipeline

    def engine_started(self):
        """
        引擎启动
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: engine_started'
        pass

    def engine_stopped(self):
        """
        引擎停止
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: engine_stopped'
        pass

    def item_scraped(self, item, response, spider):
        """
        数据保留（通过管道）
        :param item:
        :param response:
        :param spider:
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: item_scraped'
        pass

    def item_dropped(self, item, response, exception, spider):
        """
        数据丢弃（移出管道）
        :param item:
        :param response:
        :param exception:
        :param spider:
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: item_dropped'
        pass

    def spider_opened(self, spider):
        """
        打开蜘蛛（保留蜘蛛资源）
        :param spider:
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: spider_opened'
        file_csv = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file_csv
        self.exporter = CsvItemExporter(file_csv)
        self.exporter.start_exporting()

    def spider_closed(self, spider, reason):
        """
        关闭蜘蛛（释放蜘蛛资源）
        :param spider:
        :param reason: finished/cancelled/shutdown
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: spider_closed'
        self.exporter.finish_exporting()
        file_csv = self.files.pop(spider)
        file_csv.close()

    def spider_idle(self, spider):
        """
        蜘蛛空闲
        :param spider:
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: spider_idle'
        pass

    def spider_error(self, failure, response, spider):
        """
        蜘蛛错误
        :param failure:
        :param response:
        :param spider:
        :return:
        """
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: spider_error'
        pass

    def request_scheduled(self, request, spider):
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: request_scheduled'
        pass

    def request_dropped(self, request, spider):
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: request_dropped'
        pass

    def response_received(self, response, request, spider):
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: response_received'
        pass

    def response_downloaded(self, response, request, spider):
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Signals: response_downloaded'
        pass

    def process_item(self, item, spider):
        print time.strftime("%Y-%m-%d %H:%M:%S"), 'Pipeline   Process: process_item'
        if randint(1, 4) == 2:
            raise DropItem("Spider : %s, DropItem : %r" % (spider.name, item))
        self.exporter.export_item(item)
        return item


"""
✗ scrapy crawl ip_cn
信号顺序测试结果（单个蜘蛛4个抓取入口）

request_dropped 信号没有捕捉到

结果如下：

Scrapy 1.0.3 started
Optional features available
Overridden settings
Enabled extensions
Enabled downloader middlewares
Enabled spider middlewares
Enabled item pipelines

2017-05-02 09:40:51 Signals: spider_opened                  # 打开蜘蛛（保留蜘蛛资源）
2017-05-02 09:40:51 Signals: engine_started                 # 引擎启动

2017-05-02 09:40:51 Signals: request_scheduled              # 引擎调度请求
2017-05-02 09:40:51 Middleware Process: process_request                             # 中间件处理请求
2017-05-02 09:40:51 Signals: request_scheduled              # 引擎调度请求
2017-05-02 09:40:51 Middleware Process: process_request                             # 中间件处理请求
2017-05-02 09:40:51 Signals: request_scheduled              # 引擎调度请求
2017-05-02 09:40:51 Middleware Process: process_request                             # 中间件处理请求
2017-05-02 09:40:51 Signals: request_scheduled              # 引擎调度请求
2017-05-02 09:40:51 Middleware Process: process_request                             # 中间件处理请求

2017-05-02 09:40:57 Signals: response_downloaded            # 下载响应
2017-05-02 09:40:57 Middleware Process: process_response                            # 中间件处理响应
2017-05-02 09:40:57 Signals: response_received              # 接收响应
2017-05-02 09:40:57 Pipeline Process: process_item                                  # 管道处理数据
2017-05-02 09:40:57 Signals: item_scraped                   # 数据保留（通过管道）

2017-05-02 09:40:58 Signals: response_downloaded
2017-05-02 09:40:58 Signals: response_received
2017-05-02 09:40:58 Pipeline Process: process_item
2017-05-02 09:40:58 Signals: item_scraped / item_dropped

2017-05-02 09:40:59 Signals: response_downloaded
2017-05-02 09:40:59 Signals: response_received
2017-05-02 09:41:00 Pipeline Process: process_item
2017-05-02 09:41:00 Signals: item_scraped / item_dropped

2017-05-02 09:41:02 Signals: response_downloaded
2017-05-02 09:41:02 Signals: response_received
2017-05-02 09:41:02 Pipeline Process: process_item
2017-05-02 09:41:02 Signals: item_scraped / item_dropped

2017-05-02 09:41:02 Signals: spider_idle                    # 蜘蛛空闲
2017-05-02 09:41:02 Signals: spider_closed                  # 关闭蜘蛛（释放蜘蛛资源）
2017-05-02 09:41:02 Signals: engine_stopped                 # 引擎停止
"""
