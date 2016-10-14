# -*- coding: utf-8 -*-
import scrapy
import urlparse
import time
from app.items.v4 import ServiceV4Item
from app.rules import *


base_city_ist = [
    'sh'
]

# 分类就是手机品牌
base_cate_list = [
    'shoujiweixiu'
]


class Crawl58ServiceSjwxV4Spider(scrapy.Spider):
    name = "crawl58_service_sjwx_v4"
    allowed_domains = ["58.com"]
    start_urls = [
        'http://sh.58.com/shoujiweixiu/'  # 手机维修
    ]

    def parse(self, response):
        """
        准备入口数据
        """
        # 服务范围
        # print response.url
        city_list = set()  # 服务范围
        cate_list = set()  # 服务项目
        res_city_list = response.xpath('//*[@id="relateSelect"]//a/@href').extract()
        for res_city in res_city_list:
            city = city_re_compile.findall(res_city)
            if not city:
                continue
            city_list.add(city[0] if city else None)
        city_list -= set(base_city_ist)

        # 服务项目（品牌）
        res_cate_list = response.xpath('//dd[@id="shoujipinpai"]/a/@href').extract()
        for res_cate in res_cate_list:
            cate = cate_re_compile.findall(res_cate)
            if not cate:
                continue
            cate_list.add(cate[0] if cate else None)
        cate_list -= set(base_cate_list)

        # 新增入口页面
        new_start_urls = ['http://%s/%s/%s/pn1/' % (urlparse.urlparse(response.url).netloc, city, cate) for city in
                          city_list for cate in cate_list]
        for url in new_start_urls:
            # 抓取入口首页
            yield scrapy.Request(url=url, callback=self.parse_list, priority=0)

    def parse_list(self, response):
        """
        抓取列表
        """
        # 获取当前页码
        page_num_result = page_num_re_compile.findall(response.url)
        fetch_page_num = page_num_result[0] if page_num_result else ''

        # 获取当前列表页面 城市、分类 编码
        url_res = urlparse.urlparse(response.url)
        fetch_city_code = url_res.netloc.replace('.58.com', '')
        fetch_cate_code = url_res.path.strip('/').split('/')[1]

        # 获取列表
        trs = response.xpath('//table[@id="jingzhun"]//tr//div[@class="tdiv"]')
        for tr in trs:
            link_list = tr.xpath('.//a[@class="t"]/@href')
            service_link = link_list.extract_first(default='')

            if service_link:
                # 公司名称
                company_name = tr.xpath('.//p[contains(@class, "seller")]//a[@class="u"]/text()').extract_first(
                    default='').strip()
                # 抓取详情页面
                yield scrapy.Request(
                    url=service_link,
                    callback=self.parse_detail,
                    priority=100,
                    meta={
                        'fetch_list_url': response.url,
                        'fetch_page_num': fetch_page_num,
                        'fetch_city_code': fetch_city_code,
                        'fetch_cate_code': fetch_cate_code,
                        'company_name': company_name
                    }
                )
        # 下一页
        next_url = response.xpath('//div[@class="pager"]/a[@class="next"]/@href').extract_first(default='')
        next_url = urlparse.urljoin(response.url, next_url)
        if next_url == response.url:
            print '当前条件列表页最后一页：%s' % response.url
        else:
            yield scrapy.Request(url=next_url, callback=self.parse_list, priority=10)

    def parse_detail(self, response):
        """
        抓取详细页面
        """
        # print response.url

        # 处理链接
        url_res = urlparse.urlparse(response.url)
        fetch_detail_url = response.url.replace('?%s' % url_res.query, '')

        # 获取页面信息
        service_title = response.xpath('//div[@class="mainTitle"]/h1/text()').extract_first(default='').strip()
        service_pub_date = response.xpath('//div[@id="index_show"]//li[@class="time"]/text()').extract_first(
            default='').strip()
        service_district = ' '.join(
            [item.strip('') for item in response.xpath('//div[contains(@class, "quyuline")]/a/text()').extract()])
        contact_user = response.xpath('//div[contains(@class, "mg_l_7")]/a/text()').extract_first(default='').strip()
        contact_phone = response.xpath('//span[@class="l_phone"]/text()').extract_first(default='').strip()

        company_district = ' - '.join([item.strip('- ') for item in response.xpath(
            '//div[@class="description"]/div[@class="newinfo"]/ul/li[1]/a/text()').extract()])
        company_name = response.xpath('//div[@class="userinfo"]/h2/text()').extract_first(default='').strip()
        company_address_re_list = response.xpath('//div[@class="userinfo"]/ul[@class="uinfolist"]/li').re(
            company_address_re_compile)
        company_address = company_address_re_list[0].strip() if company_address_re_list else ''
        company_reg_date_re_list = response.xpath('//div[@class="userinfo"]/ul[@class="uinfolist"]/li').re(
            company_reg_date_re_compile)
        company_reg_date = company_reg_date_re_list[0].strip().replace('.', '-') if company_reg_date_re_list else ''
        company_home_page = response.xpath('//li[@class="weizhan"]//div[@class="zhan_r_con"]/a/@href').extract_first(
            default='').strip()

        # 认证状态（个人、企业）
        verified_personal = int(
            response.xpath('//span[@class="ico-rzv-o"]/@title').extract_first(default='').strip() == u'个人身份已认证')
        verified_company = int(
            response.xpath('//span[@class="ico-rzv-b"]/@title').extract_first(default='').strip() == u'企业执照已认证')

        fetch_time = time.strftime("%Y-%m-%d %H:%M:%S")  # 抓取时间

        # 保存服务信息
        item_service = ServiceV4Item()
        item_service['service_title'] = service_title  # 服务名称
        item_service['service_pub_date'] = service_pub_date  # 服务发布日期
        item_service['service_district'] = service_district  # 服务地区
        item_service['contact_user'] = contact_user  # 联系人
        item_service['contact_phone'] = contact_phone  # 电话
        item_service['company_name'] = company_name or response.meta['company_name']  # 公司名称
        item_service['company_home_page'] = company_home_page  # 公司主页
        item_service['company_district'] = company_district  # 公司地区
        item_service['company_address'] = company_address  # 公司地址
        item_service['company_reg_date'] = company_reg_date  # 公司注册日期
        item_service['fetch_platform'] = 5  # 抓取平台
        item_service['fetch_city_code'] = response.meta['fetch_city_code']  # 抓取城市编码
        item_service['fetch_cate_code'] = response.meta['fetch_cate_code']  # 抓取分类编码
        item_service['fetch_detail_url'] = fetch_detail_url  # 抓取详情链接
        item_service['fetch_list_url'] = response.meta['fetch_list_url']  # 抓取列表链接
        item_service['fetch_page_num'] = response.meta['fetch_page_num']  # 抓取列表页码
        item_service['verified_personal'] = verified_personal  # 个人验证标识
        item_service['verified_company'] = verified_company  # 公司验证标识
        item_service['export_flag'] = 0  # 导出标识
        item_service['create_time'] = fetch_time  # 创建时间
        item_service['update_time'] = fetch_time  # 更新时间

        yield item_service


# scrapy genspider crawl58_service_sjwx_v4 58.com

# scrapy crawl crawl58_service_sjwx_v4 -s JOBDIR=crawls/app/crawl58_service_sjwx_v4

