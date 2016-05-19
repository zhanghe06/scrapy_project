#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: local.py
@time: 16-3-10 下午5:10
"""


import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)+'/../')

# 数据库
DB_CRAWL = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '123456',
    'db': 'test',
    'port': 3306
}
SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
    (DB_CRAWL['user'], DB_CRAWL['passwd'], DB_CRAWL['host'], DB_CRAWL['port'], DB_CRAWL['db'])
SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5

# 代理列表（包含协议，域名，端口）
PROXY_LIST = ['http://192.168.2.158:3128']
