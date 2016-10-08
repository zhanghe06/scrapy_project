# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ServiceV3Item(scrapy.Item):
    source_type = scrapy.Field()  # 来源网站
    picture = scrapy.Field()  # 服务图片 service_logo
    publisher = scrapy.Field()  # 发布人 service_contacts
    title = scrapy.Field()  # 服务标题 service_title
    provider_name = scrapy.Field()  # 服务商、公司名称
    source_cid = scrapy.Field()  # 原始cid
    summary = scrapy.Field()  # 服务简介 service_summary
    phone = scrapy.Field()  # 联系电话 service_phone
    city_id = scrapy.Field()  # 城市id
    city_name = scrapy.Field()  # 城市名称
    industry = scrapy.Field()  # 行业
    source_sid = scrapy.Field()  # 原始service_id
    classify_url = scrapy.Field()  # 来源列表页面
    detail_url = scrapy.Field()  # 详细页的url  # 服务链接 service_url
    url_md5 = scrapy.Field()  # 详细页的url
    page_num = scrapy.Field()  # 页码
    service_area = scrapy.Field()  # 服务区域
    identity_verify = scrapy.Field()  # 个人身份认证状态 service_auth_person
    pub_time = scrapy.Field()  # 发布时间
    fetch_time = scrapy.Field()  # 抓取时间
    clean_flag = scrapy.Field()  # 清洗标记


class ProviderV3Item(scrapy.Item):
    source_type = scrapy.Field()  # 来源网站
    full_name = scrapy.Field()  # 服务商名称 service_company_name
    address = scrapy.Field()  # 服务商地址
    service_circle = scrapy.Field()  # 服务商圈
    city_id = scrapy.Field()  # 城市id
    city_name = scrapy.Field()  # 城市名
    logo_path = scrapy.Field()  # 公司logo
    homepage = scrapy.Field()  # 公司链接 service_company_url
    industry = scrapy.Field()  # 公司行业
    attr = scrapy.Field()  # 属性、分类
    scale = scrapy.Field()  # 规模
    source_cid = scrapy.Field()  # 原始cid
    classify_url = scrapy.Field()  # 来源列表页面
    fetch_time = scrapy.Field()  # 抓取时间
    clean_flag = scrapy.Field()  # 清洗标记
    phone = scrapy.Field()  # 联系电话
    star = scrapy.Field()  # 星级 service_score
    reserve = scrapy.Field()  # 预约人数 service_reserve
    evaluate = scrapy.Field()  # 评价次数 service_evaluate
    license_verify = scrapy.Field()  # 营业执照认证状态，公司认证状态 service_auth_company
    vip58_year = scrapy.Field()  # 网邻通年数 service_wlt_years
    vip58_index = scrapy.Field()  # 网邻通指数 service_wlt_index
