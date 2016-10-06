# -*- coding: utf-8 -*-
import scrapy
import re
import urlparse
import time
from app.items import PositionItem


class Crawl58Spider(scrapy.Spider):
    name = "crawl58"
    allowed_domains = ["58.com"]
    start_urls = [
        'http://sh.58.com/banjia/',  # 搬家
        # 'http://sh.58.com/baojie/',  # 保洁清洗
        # 'http://sh.58.com/dianqi/',  # 家电维修
        # 'http://sh.58.com/baomu/',  # 保姆/月嫂
        # 'http://sh.58.com/shoujiweixiu/',  # 手机维修
        # 'http://sz.58.com/banjia/',  # 搬家（深圳）
    ]

    city_rule = r'.*/(\w+)/\w+/$'
    cate_rule = r'.*/(\w+)/$'
    page_num_rule = r'/pn(\d+)/$'

    city_re_compile = re.compile(city_rule, re.I)
    cate_re_compile = re.compile(cate_rule, re.I)
    page_num_re_compile = re.compile(page_num_rule, re.I)

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
            city = re.compile(self.city_rule, re.I).findall(res_city)
            if not city:
                continue
            city_list.add(city[0] if city else None)
        # 服务项目
        res_cate_list = response.xpath('//*[@id="ObjectType"]//a/@href').extract()
        for res_cate in res_cate_list:
            cate = re.compile(self.cate_rule, re.I).findall(res_cate)
            if not cate:
                continue
            cate_list.add(cate[0] if cate else None)
        # 新增入口页面
        new_start_urls = ['http://%s/%s/%s/pn1/' % (urlparse.urlparse(response.url).netloc, city, cate) for city in city_list for cate in cate_list]
        for url in new_start_urls:
            # 抓取入口首页
            yield scrapy.Request(url=url, callback=self.parse_list, priority=0)

    def parse_list(self, response):
        """
        抓取列表
        """
        # 获取当前页码
        page_num_result = self.page_num_re_compile.findall(response.url)
        page_num = page_num_result[0] if page_num_result else ''

        # 获取列表
        trs = response.xpath('//div[@id="infolist"]//div[contains(@class, "listWrap")]')
        for tr in trs:
            link_list = tr.xpath('//div[@class="listInfo"]/a[@class="t"]/@href')
            service_link = link_list.extract_first(default='')
            # print service_link
            if service_link:
                # 获取服务商logo
                service_logo = tr.xpath('//div[@class="mainTitle"]/h1/text()').extract_first(default='').strip()
                # 认证状态（企业、个人）
                qiye_v = int(tr.xpath('//i[contains(@class, "qiye")]/@title').extract_first(default='').strip() == u'企业营业执照已认证')
                geren_v = int(tr.xpath('//i[contains(@class, "geren")]/@title').extract_first(default='').strip() == u'个人身份已认证')
                # 抓取详情页面
                yield scrapy.Request(
                    url=service_link,
                    callback=self.parse_detail,
                    priority=100,
                    meta={
                        'list_url': response.url,
                        'page_num': page_num,
                        'service_logo': service_logo,
                        'qiye_v': qiye_v,
                        'geren_v': geren_v
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
        service_url = response.url.replace('?%s' % url_res.query, '')
        city_name = url_res.netloc.replace('.58.com', '')
        cate_name = url_res.path.strip('/').split('/')[0]
        # 获取页面信息
        service_title = response.xpath('//div[@class="mainTitle"]/h1/text()').extract_first(default='').strip()
        pub_time = response.xpath('//div[@id="index_show"]//li[@class="time"]/text()').extract_first(default='').strip()
        service_district = response.xpath('//div[contains(@class, "quyuline")]/a/text()').extract_first(default='').strip()
        # service_cate = response.xpath('//a[@class="hqgs"]/text()').extract_first(default='').strip()
        service_contacts = response.xpath('//div[contains(@class, "mg_l_7")]/a/text()').extract_first(default='').strip()
        service_phone = response.xpath('//span[@class="l_phone"]/text()').extract_first(default='').strip()
        company_district = ' - '.join([item.strip('- ') for item in response.xpath('//div[@class="description"]/div[@class="newinfo"]/ul/li[1]/a/text()').extract()])
        company_address = response.xpath('//div[@class="description"]/div[@class="newinfo"]/ul/li[1]/span[@class="adr"]/text()').extract_first(default='').strip('- ')
        company_name = response.xpath('//section[@id="side"]/div[@class="userinfo"]/h2/text()').extract_first(default='').strip()
        company_home_page = response.xpath('//li[@class="weizhan"]//div[@class="zhan_r_con"]/a/@href').extract_first(default='').strip()

        # 保存服务信息
        item_position = PositionItem()
        item_position['title'] = service_title
        item_position['city'] = service_district
        item_position['address'] = company_address
        item_position['industry'] = ''
        item_position['email'] = ''
        item_position['phone'] = service_phone
        item_position['description'] = ''
        item_position['detail_url'] = service_url
        item_position['list_url'] = response.meta['list_url']
        item_position['create_time'] = pub_time
        item_position['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S")
        #
        # item_service['source_type'] = 5  # 来源网站
        # item_service['picture'] = response.meta['service_logo']
        # item_service['publisher'] = service_contacts
        # item_service['title'] = service_title
        # item_service['provider_name'] = company_name  # 服务商、公司名称
        # item_service['source_cid'] = md5(company_name)  # 原始cid
        # item_service['summary'] = ''  # 服务简介
        # item_service['phone'] = service_phone
        # item_service['city_id'] = ''  # 城市id
        # item_service['city_name'] = city_name  # 城市名称
        # item_service['industry'] = ''  # 行业
        # item_service['source_sid'] = cate_name  # 原始service_id
        # item_service['classify_url'] = response.meta['list_url']  # 来源页面url
        # item_service['detail_url'] = service_url
        # item_service['url_md5'] = md5(service_url)  # 详细页的url
        # item_service['page_num'] = response.meta['page_num']  # 页码
        # item_service['service_area'] = service_district
        # item_service['identity_verify'] = response.meta['geren_v']
        # item_service['pub_time'] = pub_time  # '1970-01-01 08:00:00'  # 发布时间
        # item_service['fetch_time'] = time.strftime("%Y-%m-%d %H:%M:%S")  # 抓取时间
        # item_service['clean_flag'] = 0  # 清洗标记

        # 保存公司信息
        # item_company = CompanyV3Item()
        # item_company['source_type'] = 5  # 来源网站
        # item_company['full_name'] = company_name  # 服务商名称
        # item_company['address'] = company_address  # 服务商地址
        # item_company['service_circle'] = company_district  # 服务商圈
        # item_company['city_id'] = ''  # 城市id
        # item_company['city_name'] = city_name  # 城市名
        # item_company['logo_path'] = ''  # 公司logo
        # item_company['homepage'] = company_home_page  # 公司链接
        # item_company['industry'] = ''  # 公司行业
        # item_company['attr'] = ''  # 属性、分类
        # item_company['scale'] = ''  # 规模
        # item_company['source_cid'] = md5(company_name)  # 原始cid
        # item_company['phone'] = service_phone  # 联系电话
        # item_company['star'] = 0  # 星级
        # item_company['reserve'] = 0  # 预约人数
        # item_company['evaluate'] = 0  # 评价次数
        # item_company['license_verify'] = response.meta['qiye_v']  # 营业执照认证状态，公司认证状态
        # item_company['vip58_year'] = 0  # 网邻通年数
        # item_company['vip58_index'] = 0  # 网邻通指数
        # item_company['classify_url'] = response.meta['list_url']  # 来源页面url
        # item_company['url_md5'] = md5(response.meta['list_url'])  # 来源页面url 的md5
        # item_company['fetch_time'] = time.strftime("%Y-%m-%d %H:%M:%S")  # 抓取时间
        # item_company['clean_flag'] = 0  # 清洗标记

        yield item_position
        # yield item_company


# scrapy genspider crawl58 58.com

# scrapy crawl crawl58

# 每个分类最大页码 70
# 每页最大记录 40


# 方案一：
# 页面靠前的优先抓取
# 入口 800
# 详情 600
# 列表 400