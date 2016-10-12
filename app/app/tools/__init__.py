# -*- coding: utf-8 -*-
import hashlib


def md5(source_str):
    """
    md5加密
    :param source_str:
    :return:
    """
    return hashlib.md5(source_str.encode("utf8") if isinstance(source_str, unicode) else source_str).hexdigest()


# 58 分类
cate_map = {
    # 手机维修 http://sh.58.com/shoujiweixiu/
    'pgshj':        '手机维修',  # iphone,
    'sxshj':        '手机维修',  # 三星,
    'nokiashj':     '手机维修',  # 诺基亚,
    'mtllshj':      '手机维修',  # 摩托罗拉,
    'sashj':        '手机维修',  # 索尼爱立信,
    'xpshj':        '手机维修',  # 夏普,
    'lgshj':        '手机维修',  # LG,
    'dpdshj':       '手机维修',  # 多普达,
    'lxshj':        '手机维修',  # 联想,
    'htcwx':        '手机维修',  # HTC,
    'xiaomisjwx':   '手机维修',  # 小米,
    'meizuwx':      '手机维修',  # 魅族,
    'heimeiwx':     '手机维修',  # 黑莓,
    'huaweiwx':     '手机维修',  # 华为,
    'zhongxingwx':  '手机维修',  # 中兴,
    'kupaiwx':      '手机维修',  # 酷派,
    'tianyuwx':     '手机维修',  # 天语,
    'jinliwx':      '手机维修',  # 金立,

    # 家电维修 http://sh.58.com/dianqi/
    'kongtiao':           '空调维修/移机',
    'reshuiqiweixiu':     '热水器维修',
    'chufangwx':          '厨房家电维修',
    'xiyijiweixiu':       '洗衣机维修',
    'bingxiangweixiu':    '冰箱维修',
    'dianshiweixiu':      '电视维修',
    'yixiangwx':          '影音家电维修',
    'xiaojiadianwx':      '小家电维修',

    # 保洁清洗 http://sh.58.com/baojie/
    'kongtiaoqingxi':     '空调清洗',
    'kaihuangbaojie':     '开荒保洁',
    'richangbaojie':      '物业保洁',
    'ditan':              '地毯清洗',
    'jiatingbaojie':      '家庭保洁',
    'boliqixi':           '玻璃清洗',
    'youyan':             '油烟机清洗',
    'scfanxin':           '石材翻新/养护',
    'kongqijinghua':      '空气净化',
    'bizhiqx':            '壁纸清洗',
    'dbdala':             '地板打蜡',
    'shafaby':            '沙发清洗',
    'dengjubaojie':       '灯具清洗',
    'gaokongqingxi':      '高空清洗',
    'chuchongchuyi':      '除虫除蚁',
    'cizhuanmeifeng':     '瓷砖美缝',

    # 保姆/月嫂 http://sh.58.com/baomu/
    'zhongdiangong':      '钟点工',
    'bmu':                '保姆',
    'yuyingshi':          '育婴师/育儿嫂',
    'yuesao':             '月嫂',
    'yiliaopeihu':        '陪护',
    'cuirushi':           '催乳师',
    'sewai':              '涉外家政',
    'guanjia':            '管家',

    # 搬家 http://sh.58.com/banjia/
    'juminbj':            '居民搬家',
    'kongtiaochaizhuang': '空调移机',
    'banjiabanchang':     '搬家搬场',
    'xiaoxingbanjia':     '小型搬家',
    'gongsibanjia':       '公司搬家',
    'changtubanjia':      '长途搬家搬运',
    'gangqinby':          '钢琴搬运',
    'qizhongdiaozhuang':  '起重吊装',
    'shebeibanqian':      '设备搬迁',
    'jiajuchaizhuang':    '家具拆装',
    'guojibanjia':        '国际搬家',
}
