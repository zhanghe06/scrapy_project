#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: gen.py
@time: 16-5-18 下午4:22
"""


import os
import sys
from sqlalchemy.ext.declarative.api import DeclarativeMeta
from sqlalchemy.inspection import inspect
from config import BASE_DIR

# MySQL
# from config import SQLALCHEMY_DATABASE_URI_MYSQL as SQLALCHEMY_DATABASE_URI
# PostgreSQL
from config import SQLALCHEMY_DATABASE_URI_PG as SQLALCHEMY_DATABASE_URI


def gen_models():
    """
    创建 models
    $ python gen.py gen_models
    """
    file_path = os.path.join(BASE_DIR, 'models.py')
    cmd = 'sqlacodegen %s --outfile %s' % (SQLALCHEMY_DATABASE_URI, file_path)

    output = os.popen(cmd)
    result = output.read()
    print result

    # 更新 model 文件
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # 新增 model 转 dict 方法
    with open(file_path, 'w') as f:
        lines.insert(9, 'def to_dict(self):\n')
        lines.insert(10, '    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}\n')
        lines.insert(11, '\n')
        lines.insert(12, 'Base.to_dict = to_dict\n')
        lines.insert(13, '\n\n')
        f.write(''.join(lines))


def gen_items():
    """
    创建 items
    $ python gen.py gen_items > items.py
    字段规则： 去除自增主键，非自增是需要的。
    """
    import models
    model_list = [k for k, v in models.__dict__.iteritems() if isinstance(v, DeclarativeMeta) and k != 'Base']
    # print json.dumps(model_list, indent=4)
    print '''# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy'''
    for model_item in model_list:
        result = eval(model_item)().to_dict()
        model_pk = inspect(eval(model_item)).primary_key[0]
        print '\n'
        print 'class %sItem(scrapy.Item):' % model_item
        print '    """'
        print '    primary_key： %s' % model_pk
        print '    """'
        for field_name in result.keys():
            print '    %s = scrapy.Field()' % field_name


def run():
    """
    入口
    """
    # print sys.argv
    try:
        if len(sys.argv) > 1:
            fun_name = eval(sys.argv[1])
            fun_name()
        else:
            print '缺失参数\n'
            usage()
    except NameError, e:
        print e
        print '未定义的方法[%s]' % sys.argv[1]


def usage():
    print """
创建 models
$ python gen.py gen_models

创建 items
$ python gen.py gen_items > items.py
"""


if __name__ == '__main__':
    run()
