#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: exporter_xml.py
@time: 2017/4/28 下午2:22
"""

from scrapy import signals
from scrapy.exporters import XmlItemExporter


class XmlExportPipeline(object):
    """
    app.pipelines.exporter_xml.XmlExportPipeline
    """
    def __init__(self):
        self.files = {}
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file_xml = open('%s_items.xml' % spider.name, 'w+b')
        self.files[spider] = file_xml
        self.exporter = XmlItemExporter(file_xml)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file_xml = self.files.pop(spider)
        file_xml.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
