# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ServiceV4Item(scrapy.Item):
    service_title     = scrapy.Field()  # 服务名称
    service_pub_date  = scrapy.Field()  # 服务发布日期
    service_district  = scrapy.Field()  # 服务地区
    contact_user      = scrapy.Field()  # 联系人
    contact_phone     = scrapy.Field()  # 电话
    company_name      = scrapy.Field()  # 公司名称
    company_home_page = scrapy.Field()  # 公司主页
    company_district  = scrapy.Field()  # 公司地区
    company_address   = scrapy.Field()  # 公司地址
    company_reg_date  = scrapy.Field()  # 公司注册日期
    fetch_platform    = scrapy.Field()  # 抓取平台
    fetch_city_code   = scrapy.Field()  # 抓取城市编码
    fetch_cate_code   = scrapy.Field()  # 抓取分类编码
    fetch_detail_url  = scrapy.Field()  # 抓取详情链接
    fetch_list_url    = scrapy.Field()  # 抓取列表链接
    fetch_page_num    = scrapy.Field()  # 抓取列表页码
    verified_personal = scrapy.Field()  # 个人验证标识
    verified_company  = scrapy.Field()  # 公司验证标识
    export_flag       = scrapy.Field()  # 导出标识
    create_time       = scrapy.Field()  # 创建时间
    update_time       = scrapy.Field()  # 更新时间
