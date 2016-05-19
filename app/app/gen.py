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
from config import BASE_DIR, SQLALCHEMY_DATABASE_URI, DB_CRAWL


def gen_model():
    """
    创建model
    $ python gen.py gen_model
    """
    cmd = 'sqlacodegen %s --outfile %s' % (SQLALCHEMY_DATABASE_URI, os.path.join(BASE_DIR, 'models.py'))
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


def create_db():
    """
    建库 建表
    $ python gen.py create_db
    """
    cmd = 'mysql -h%s -u%s -p%s < %s' % (DB_CRAWL['host'], DB_CRAWL['user'], DB_CRAWL['passwd'], os.path.join(BASE_DIR, 'db_create.sql'))
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


def dump_db():
    """
    备份数据
    $ python gen.py dump_db
    """
    cmd = 'mysqldump -h%s -u%s -p%s %s > %s' % (DB_CRAWL['host'], DB_CRAWL['user'], DB_CRAWL['passwd'], DB_CRAWL['db'], os.path.join(BASE_DIR, 'db_dump.sql'))
    print cmd
    output = os.popen(cmd)
    result = output.read()
    print result


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
创建(更新)model
$ python gen.py gen_model

建库 建表（初始化数据库）
$ python gen.py create_db
"""


if __name__ == '__main__':
    run()
