#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: test_dict.py
@time: 2016/10/13 下午1:44
"""


def func():
    list_a = [1, 2, 3, 4, 5]
    print dict(zip(list_a, [1]*len(list_a)))


if __name__ == '__main__':
    func()
