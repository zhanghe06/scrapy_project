#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_db_pool.py
@time: 2017/6/7 下午4:37
"""


import sys
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import SQLALCHEMY_DATABASE_URI_PG
from app.config import SQLALCHEMY_POOL_SIZE


engine_pg = create_engine(
    SQLALCHEMY_DATABASE_URI_PG,
    pool_size=SQLALCHEMY_POOL_SIZE,
    max_overflow=0
)
db_session_pg = sessionmaker(engine_pg, autocommit=True)
# db_session_pg = sessionmaker(engine_pg, autocommit=False)

db_session = db_session_pg()


def run():
    try:
        if len(sys.argv) > 2:
            fun_name = eval(sys.argv[1])
            fun_name(sys.argv[2])
        else:
            print '缺失参数'
    except NameError, e:
        print e
        print '未定义的方法[%s]' % sys.argv[1]
    except KeyboardInterrupt:
        db_session.close_all()


def test_01(name):
    """
    外层建立连接
    :param name:
    :return:
    """
    while 1:
        # raw_input()
        print name, id(db_session)
        sql = 'SELECT now() as t;'
        print db_session.execute(sql).first()['t']
        # db_session.commit()
        # db_session.close()  # 释放连接
        # db_session.close_all()


def test_02(name):
    """
    单独建立连接
    autocommit=False
    如果连接不提交/释放，会不断创建新连接，直到超出连接池大小限制抛异常
    autocommit=true
    则不会
    :param name:
    :return:
    """
    while 1:
        raw_input()
        db_session_02 = db_session_pg()
        print name, id(db_session_02)
        sql = 'SELECT now() as t, pg_sleep(1);'
        print db_session_02.execute(sql).first()['t']
        # db_session_02.commit()
        # db_session_02.close()  # 释放连接
        # db_session_02.close_all()


def test_03(name):
    """
    测试异常
    autocommit=False
    如果连接不提交/释放，会不断创建新连接，直到超出连接池大小限制抛异常
    :param name:
    :return:
    """
    while 1:
        raw_input()
        db_session_02 = db_session_pg()
        print name, id(db_session_02)
        sql = 'SELECT 1/0 as t, pg_sleep(1);'
        print db_session_02.execute(sql).first()['t']
        # db_session_02.commit()
        # db_session_02.close()  # 释放连接
        # db_session_02.close_all()


def test_04(name):
    """
    测试批量操作
    autocommit=False
    如果连接不提交/释放，会不断创建新连接，直到超出连接池大小限制抛异常
    :param name:
    :return:
    """
    while 1:
        raw_input()
        print name, id(db_session)
        sql = 'SELECT 1/0 as t, pg_sleep(1);'
        print db_session.execute(sql).first()['t']
        # db_session_02.commit()
        # db_session_02.close()  # 释放连接
        # db_session_02.close_all()


if __name__ == '__main__':
    run()


"""
python app/tests/test_db_pool.py test_01 1
python app/tests/test_db_pool.py test_02 1
python app/tests/test_db_pool.py test_03 1

wl_crawl=# SELECT COUNT(*) from pg_stat_activity;
"""


"""
测试用例：
1、autocommit=False, session commit/close，再次查询，查询结果才会更新
1、autocommit=True,  session commit，会抛出异常：raise sa_exc.InvalidRequestError("No transaction is begun.")
2、autocommit=True,  session close 再次使用 session 可查询，结果更新


结论：
autocommit=True
session 不能 commit，除非声明事务
session 可以 close

"""
