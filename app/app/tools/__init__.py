# -*- coding: utf-8 -*-
import hashlib


def md5(source_str):
    """
    md5加密
    :param source_str:
    :return:
    """
    return hashlib.md5(source_str.encode("utf8") if isinstance(source_str, unicode) else source_str).hexdigest()
