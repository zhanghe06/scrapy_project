#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: db.py
@time: 16-5-18 上午11:43
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_POOL_SIZE


# 初始化数据库连接:
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=SQLALCHEMY_POOL_SIZE)

# 创建 db_session
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

if __name__ == '__main__':
    pass
