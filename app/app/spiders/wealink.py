# -*- coding: utf-8 -*-
import scrapy


class WealinkSpider(scrapy.Spider):
    name = "wealink"
    allowed_domains = ["www.wealink.com"]
    start_urls = (
        'http://www.wealink.com/passport/login',
    )
    login_url = 'http://www.wealink.com/passport/login'
    login_form_data = {
        'callback': '/',
        'username': '13818732593',
        'password': 'xxxxxx'
    }

    def parse(self, response):
        """
        入口
        :param response:
        :return:
        """
        return self.login()
        # return self.login_with_info(response)

    def login(self):
        """
        通用提交方式
        :return:
        """
        return scrapy.FormRequest(
            url=self.login_url,
            formdata=self.login_form_data,
            callback=self.after_login
        )

    def login_with_info(self, response):
        """
        有隐藏域表单信息时的提交方式
        :param response:
        :return:
        """
        return scrapy.FormRequest.from_response(
            response,
            formdata=self.login_form_data,
            callback=self.after_login
        )

    def after_login(self, response):
        """
        获取登录状态
        :param response:
        :return:
        """
        print response
        if response.url in ['http://www.wealink.com', 'http://www.wealink.com/']:
            print '登录成功'
        if response.url in ['http://www.wealink.com/passport/login', 'http://www.wealink.com/passport/login/']:
            print '登录失败'
