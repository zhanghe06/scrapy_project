#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2016/10/14 上午10:36
"""


import re


__all__ = [
    'city_re_compile',
    'cate_re_compile',
    'page_num_re_compile',
    'company_address_re_compile',
    'company_reg_date_re_compile'
]


city_rule = r'.*/(\w+)/\w+/$'
cate_rule = r'.*/(\w+)/$'
page_num_rule = r'/pn(\d+)/$'
company_address_rule = ur'<i>地　　址：</i>\s*<p>(.*)</p>'
company_reg_date_rule = ur'<i>注册时间：</i>\s*<p>(.*)</p>'


city_re_compile = re.compile(city_rule, re.I)
cate_re_compile = re.compile(cate_rule, re.I)
page_num_re_compile = re.compile(page_num_rule, re.I)
company_address_re_compile = re.compile(company_address_rule, re.I)
company_reg_date_re_compile = re.compile(company_reg_date_rule, re.I)
