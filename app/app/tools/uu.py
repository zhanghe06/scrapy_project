#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: uu.py
@time: 2017/4/15 下午6:01
"""


import requests
import hashlib
import uuid

from app.config import UU

# request.Headers.Add("SID",软件id);
# request.Headers.Add("HASH",md5(软件id+软件key.ToUpper()));					//32位MD5加密小写
# request.Headers.Add("UUVersion","1.0.0.1");
# request.Headers.Add("UID",UserID);											//没有登录之前，UserID就用100。登录成功后，服务器会返回UserID，之后的请求就用服务器返回的UserID
# request.Headers.Add("User-Agent", MD5(软件key.ToUpper() + UserID));			//没有登录之前，UserID就用100。登录成功后，服务器会返回UserID，之后的请求就用服务器返回的UserID


def _md5(psw):
    md5 = hashlib.md5()
    if isinstance(psw, unicode):
        psw = psw.encode("UTF-8")
    md5.update(psw)
    return md5.hexdigest()


def _get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac

MAC = _get_mac_address()


headers = {
    'SID': UU['S_ID'],
    'HASH': _md5('%s%s' % (UU['S_ID'], UU['S_KEY'].upper())),
    'UUVersion': UU['UU_VERSION'],
    'UID': UU['USER_ID'],
    'User-Agent': _md5('%s%s' % (UU['S_KEY'].upper(), UU['USER_ID']))
}


s = requests.session()


def _get_server_list():
    """
    获取(刷新)服务器列表
    1000,login.uudama.com:9000:101,upload.uuwise.net:9000:102,upload.uuwise.net:9000:103,
    域名:端口:类型
    类型101表示登录服务器，102表示上传服务器，103表示获取结果服务器，104表示备份服务器
    当upload连续出错的话，调用备份服务器,备份服务器包含所有方法，登录，上传，取得结果
    1000,表示间隔1000毫秒，请求一次getResult
    :return:
    """
    url = 'http://common.taskok.com:9000/Service/ServerConfig.aspx'
    r = s.get(url).text
    l = r.split(',')
    result = {
        'sleep_time': l.pop(0)
    }
    for info in [i.split(':') for i in l]:
        if info[-1] == u'101':
            result['url_login'] = ':'.join(info[:2])
        elif info[-1] == u'102':
            result['url_upload'] = ':'.join(info[:2])
        elif info[-1] == u'103':
            result['url_result'] = ':'.join(info[:2])
        elif info[-1] == u'104':
            result['url_backup'] = ':'.join(info[:2])
    return result


def login():
    """
    登录
    :return:
    """
    server_list = _get_server_list()
    url = server_list['url_login']
    headers_login = {
        'KEY': _md5('%s%s%s' % (UU['S_KEY'].upper(), UU['USERNAME'].upper(), MAC)),
        'UUKEY': _md5('%s%s%s' % (UU['USERNAME'].upper(), MAC, UU['S_KEY'].upper()))
    }
    headers_login.update(headers)
    user_key = s.post(url, data='', headers=headers_login).text
    return user_key

USER_KEY = login()


def get_score():
    """
    查分
    :return:
    """
    url = ''
    headers_login = {
        'UUAgent': _md5('%s%s%s' % (USER_KEY.upper(), UU['USER_ID'], UU['S_KEY'])),
        'KEY': _md5('%s%s%s' % (UU['USERNAME'].upper(), MAC, UU['S_KEY'].upper()))
    }
    headers_login.update(headers)
    s.post(url, data='', headers=headers_login)
    pass


def upload(img_path):
    """

    :return:
    """
    server_list = _get_server_list()
    url = 'http://%s/Upload/Processing.aspx' % server_list['url_upload']
    img_content = open(img_path, 'rb')
    headers_login = {
        'KEY': UU['USER_KEY'].upper(),
        'SID': UU['S_ID'],
        'SKEY': _md5('%s%s%s' % (UU['USER_KEY'].lower(), UU['S_ID'], UU['S_KEY'])),
        'Version': 100,
        'TimeOut': 25000,
        'Type': 1004,
        'IMG': img_content,
        'GUID': _md5(img_content),
    }
    headers_login.update(headers)
    user_key = s.post(url, data='', headers=headers_login).text
    return user_key


def error_report(code_id):
    """
    错误报告
    {0}为UserKey,{1}为验证码id，{2}为软件id，{3}为SKEY，值为MD5(UserKey.ToLower()+软件id+软件key)
    :return:
    """
    server_list = _get_server_list()
    url = 'http://%s/Upload/ReportError.aspx' % server_list['url_upload']
    payload = {
        'KEY': USER_KEY,
        'ID': code_id,
        'SID': UU['S_ID'],
        'SKEY': _md5('%s%s%s' % (USER_KEY.lower(), UU['S_ID'], UU['S_KEY']))
    }
    r = requests.get(url, params=payload).text
    return r


if __name__ == '__main__':
    print _get_mac_address()
