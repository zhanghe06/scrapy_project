#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: exporter_json_lines.py
@time: 2017/4/28 下午2:43
"""


from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter


class JsonLinesExportPipeline(object):
    """
    app.pipelines.exporter_json_lines.JsonLinesExportPipeline
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
        file_json_lines = open('%s_item_lines.json' % spider.name, 'w+b')
        self.files[spider] = file_json_lines
        self.exporter = JsonLinesItemExporter(file_json_lines)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file_json_lines = self.files.pop(spider)
        file_json_lines.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
