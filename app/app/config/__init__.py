#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py
@time: 16-3-10 下午5:10
"""


import os


def get_env():
    """
    获取运行环境
    """
    file_name = '/'.join((os.path.dirname(os.path.abspath(__file__)), 'config_mode'))
    with open(file_name) as f:
        env = f.read()
        if env:
            return env.strip()
        else:
            return ''


config_env = get_env()

# module = __import__(config_env)
#
# print module.db


if config_env == 'online':
    from online import *
elif config_env == 'dev':
    from dev import *
elif config_env == 'local':
    from local import *


"""
环境切换
进入项目目录
$ echo 'dev' > config/config_mode
$ echo 'online' > config/config_mode

使用配置
from config import *

在Flask中
app.config.from_object('config')
即可

注意：config/config_mode 这个文件添加至.gitignore，不需要被版本控制追踪管理
"""