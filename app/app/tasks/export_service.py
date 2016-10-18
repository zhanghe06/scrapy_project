#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: export_service.py
@time: 2016/10/13 上午11:10
"""


import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import SQLALCHEMY_DATABASE_URI_MYSQL, SQLALCHEMY_DATABASE_URI_PG, SQLALCHEMY_POOL_SIZE
from app.models.v4 import ServiceV4
from app.models.s2c import CrawlService, User
from app.tools import cate_map_v4, city_map_v4


engine_mysql = create_engine(SQLALCHEMY_DATABASE_URI_MYSQL, pool_size=SQLALCHEMY_POOL_SIZE)
DB_Session_Mysql = sessionmaker(autocommit=False, autoflush=False, bind=engine_mysql)


engine_pg = create_engine(SQLALCHEMY_DATABASE_URI_PG, pool_size=SQLALCHEMY_POOL_SIZE)
DB_Session_Pg = sessionmaker(autocommit=False, autoflush=False, bind=engine_pg)


def count_service(db_session, *args, **kwargs):
    """
    计数
    Usage:
        # 方式一
        count(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        count(User, **test_condition)
    :param db_session:
    :param args:
    :param kwargs:
    :return: 0/Number（int）
    """
    result_count = db_session.query(ServiceV4).filter(*args).filter_by(**kwargs).count()
    return result_count


def get_service_rows_by_last_id(db_session, last_pk_id, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    :param db_session:
    :param last_pk_id:
    :param limit_num:
    :param args:
    :param kwargs:
    :return: list
    """
    rows = db_session.query(ServiceV4).\
        filter(ServiceV4.id > last_pk_id, *args).\
        filter_by(**kwargs).limit(limit_num).all()
    return rows


def update_service_rows_by_ids(db_session, pk_ids, data):
    """
    根据一组主键id 批量修改数据
    """
    try:
        model_obj = db_session.query(ServiceV4).filter(ServiceV4.id.in_(pk_ids))
        result = model_obj.update(data, synchronize_session=False)
        db_session.commit()
        return result
    except Exception as e:
        db_session.rollback()
        raise e


def get_user_phone_set(db_session):
    """
    获取所有用户手机号码
    :param db_session:
    :return:
    """
    rows = db_session.query(User).all()
    return set([row.mobile for row in rows])


def insert_crawl_service_rows(db_session, data_list):
    """
    批量插入数据（遇到主键/唯一索引重复，忽略报错，继续执行下一条插入任务）
    注意：
    Warning: Duplicate entry
    警告有可能会提示：
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 17-20: ordinal not in range(128)
    处理：
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')

    sql 语句大小限制
    show VARIABLES like '%max_allowed_packet%';
    参考：http://dev.mysql.com/doc/refman/5.7/en/packet-too-large.html

    :param db_session:
    :param data_list:
    :return:
    """
    try:
        result = db_session.execute(CrawlService.__table__.insert().prefix_with('IGNORE'), data_list)
        db_session.commit()
        return result.rowcount
    except Exception as e:
        db_session.rollback()
        raise e


def is_mobile(phone):
    """
    检测是否为手机号码
    :param phone:
    :return:
    """
    if not phone:
        return 0
    prefix = phone[:1]
    if len(phone) == 11 and prefix != 0:
        return 1
    return 0


def trans_map(item_pg):
    """
    表类型转换
    :return:
    """
    item_mysql = dict()
    item_mysql['source_type'] = item_pg.fetch_platform
    item_mysql['title'] = item_pg.service_title
    item_mysql['detail_url'] = item_pg.fetch_detail_url
    item_mysql['phone'] = item_pg.contact_phone
    item_mysql['city_id'] = city_map_v4.get(item_pg.fetch_city_code, '')
    item_mysql['city_code'] = item_pg.fetch_city_code
    item_mysql['cate_id'] = cate_map_v4.get(item_pg.fetch_cate_code, '')
    item_mysql['service_type_code'] = item_pg.fetch_cate_code
    item_mysql['publisher'] = item_pg.contact_user
    item_mysql['identity_verify'] = item_pg.verified_personal
    item_mysql['provider_name'] = item_pg.company_name
    item_mysql['license_verify'] = item_pg.verified_company
    item_mysql['fetch_time'] = item_pg.create_time
    item_mysql['address'] = item_pg.company_address
    item_mysql['is_mobile'] = is_mobile(item_pg.contact_phone)
    item_mysql['page_num'] = item_pg.fetch_page_num
    item_mysql['service_circle'] = item_pg.company_district
    item_mysql['service_area'] = item_pg.service_district
    item_mysql['service_pub_date'] = item_pg.service_pub_date
    item_mysql['company_home_page'] = item_pg.company_home_page

    return item_mysql


def run():

    start_id = 0
    limit_num = 2000

    db_session_pg = DB_Session_Pg()
    db_session_mysql = DB_Session_Mysql()

    service_count = count_service(db_session_pg, **{'export_flag': 0})
    print u'服务总数：%s' % service_count

    user_phone_set = get_user_phone_set(db_session_mysql)
    print u'手机号码总数：%s' % len(user_phone_set)

    start_time = time.time()

    index = 0
    while True:
        index += 1
        try:
            index_start_time = time.time()
            service_rows = get_service_rows_by_last_id(db_session_pg, start_id, limit_num, **{'export_flag': 0})
            if not service_rows:
                end_time = time.time()
                print u'总共耗时: %.2f M' % ((end_time - start_time) / 60.0)
                break
            # 插入数据
            insert_rows = [service_row for service_row in service_rows if service_row.contact_phone not in user_phone_set]
            data_list = [trans_map(row) for row in insert_rows]
            insert_nums = insert_crawl_service_rows(db_session_mysql, data_list)
            print u'插入抓取数据: %s' % insert_nums
            # 更新字段
            service_ids = [service_row.id for service_row in service_rows]
            update_nums = update_service_rows_by_ids(db_session_pg, service_ids, {'export_flag': 1})
            print u'更新导出状态: %s' % update_nums
            index_end_time = time.time()
            less_time = (service_count - index*limit_num)*(index_end_time - index_start_time)/limit_num
            print u'剩余时间: %.2f M' % (less_time/60.0 if less_time > 0 else 0)
        except Exception as e:
            raise e
        finally:
            db_session_pg.close()
            db_session_mysql.close()


if __name__ == '__main__':
    run()
