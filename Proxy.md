## Scrapy 代理实战演示

创建代理测试spider
```
$ scrapy genspider ip ip.cn
```

设计代理程序
scrapy_project/app/app/spiders/ip.py

并修改项目配置
scrapy_project/app/app/settings.py
```
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
COOKIES_ENABLED=True
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Language': 'zh-CN,zh;q=0.8',
  'Host': 'ip.cn',
  'Referer': 'http://ip.cn/',
}
```

代理设置

1、项目目录下新建自定义中间件文件：
scrapy_project/app/app/middlewares.py
```
class HttpProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
```

2、修改配置文件，指定自定义的代理中间件
scrapy_project/app/app/settings.py
```
DOWNLOADER_MIDDLEWARES = {
   'app.middlewares.HttpProxyMiddleware': 100,
}
```

3、测试IP代理功能
(spiderenv)zhanghe@ubuntu:~/code/scrapy_project/app$ scrapy crawl ip


