#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test.py
@time: 16-5-18 下午12:03
"""


from models import User
from db import db_session


user = User(name='tom', age=20)
db_session.add(user)
db_session.commit()


if __name__ == '__main__':
    pass
