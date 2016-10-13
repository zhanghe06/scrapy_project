#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: dev.py
@time: 16-3-10 下午5:10
"""


import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)+'/../../')

# 数据库 MySQL
DB_MYSQL = {
    'host': '192.168.2.201',
    'user': 'www',
    'passwd': 'wealink.com',
    'port': 3306,
    'db': 's2c'
}
SQLALCHEMY_DATABASE_URI_MYSQL = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
    (DB_MYSQL['user'], DB_MYSQL['passwd'], DB_MYSQL['host'], DB_MYSQL['port'], DB_MYSQL['db'])

# 数据库 PostgreSQL
DB_PG = {
    'host': '192.168.2.32',
    'user': 'postgres',
    'password': 'postgres',  # 可修改 \password
    'port': 5432,
    'database': 'test'
}

SQLALCHEMY_DATABASE_URI_PG = \
    'postgresql://%s:%s@%s:%s/%s' % \
    (DB_PG['user'], DB_PG['password'], DB_PG['host'], DB_PG['port'], DB_PG['database'])

# 数据库 MongoDB
DB_MONGO = {
    'host': 'localhost',
    'port': 27017,
    'database': 'test'
}

MONGO_URI = (DB_MONGO['host'], DB_MONGO['port'])
MONGO_DATABASE = DB_MONGO['database']

SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5

REDIS = {
    'host': 'localhost',
    'port': 6379
}

# USER_AGENTS
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
]

# 代理列表（包含协议，域名，端口）
PROXY_LIST = ['http://192.168.2.158:3128']
