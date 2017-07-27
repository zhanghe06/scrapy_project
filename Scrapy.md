## 环境准备
```
virtualenv scray.env
source spiderenv/bin/activate
pip install Scrapy
```

安装过程报错
```
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 49:
```

解决办法
```
找到虚拟目录下的lib/python2.7/site.py文件
/home/zhanghe/code/wealink/wealink-web-spider/spiderenv/lib/python2.7/site.py
def setencoding():
    """Set the string encoding used by the Unicode implementation.  The
    default is 'ascii', but if you're willing to experiment, you can
    change this."""
    encoding = "ascii"  # Default value set by _PyUnicode_Init()
    if 0:  # 改成 if 1 (只修改第一个if 0 为 if 1)
```

重新安装Scrapy
```
pip uninstall Scrapy
pip install Scrapy
```

不重新安装又会报错：
```
ImportError: Twisted requires zope.interface 3.6.0 or later: no module named zope.interface.
```

安装系统依赖
```
$ sudo apt-get install libffi-dev
```

查看安装好的库文件列表
```
$ pip list
Scrapy==1.0.3
Twisted==15.4.0
argparse==1.2.1
cffi==1.2.1
characteristic==14.3.0
cryptography==1.0.1
cssselect==0.9.1
enum34==1.0.4
idna==2.0
ipaddress==1.0.14
lxml==3.4.4
pyOpenSSL==0.15.1
pyasn1==0.1.8
pyasn1-modules==0.0.7
pycparser==2.14
queuelib==1.4.2
scrapyd==1.1.0
scrapyd-client==1.0.1
service-identity==14.0.0
six==1.9.0
w3lib==1.12.0
wsgiref==0.1.2
zope.interface==4.1.2
```

导出库文件列表（仅本地）
```
$ pip freeze > requirements.txt
```

安装依赖库
```
$ pip install -r requirements.txt
```



## Scrapy使用步骤

[Scrapy 1.0 documentation](http://doc.scrapy.org/en/latest/)

[Scrapy入门教程](http://scrapy-chs.readthedocs.org/zh_CN/latest/intro/tutorial.html)


创建项目
```
$ scrapy startproject csdn
```

进入项目目录
```
$ cd csdn
```

创建一个新的spider（蜘蛛）
```
$ scrapy genspider csdnblog blog.csdn.net
```

使用刚刚创建的spider进行爬取
```
$ scrapy crawl csdnblog
```

在终端调试选择器
```
$ scrapy shell "http://blog.csdn.net/QH_JAVA/article/category/1710027"
```

保存抓取数据
```
scrapy crawl csdnblog -o items.json
```

有一个警告，先忽略
```
2015-09-21 16:44:06 [py.warnings] WARNING: :0: UserWarning: You do not have a working installation of the service_identity module: 'No module named pyasn1_modules.rfc2459'.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module and a recent enough pyOpenSSL to support it, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
```

文章列表HTML结构：
```
<div class="list_item article_item">
    <span class="link_title">
    <div class="article_description">
```

在终端测试选择器
```
>>> response.xpath('//div/h1/span').extract()
```

标题
```
>>> response.xpath('//div/h1/span/a/text()').extract()
```

标题链接
```
>>> response.xpath('//div/h1/span/a/@href').extract()
```

简介
```
>>> response.xpath('//div[@class="article_description"]/text()').extract()
```

详细页面HTML结构：
```
<div id="article_details" class="details">
    <div class="article_title">
        <h1>
            <span class="link_title">
                <a>
    <div id="article_content" class="article_content">
```

在终端测试选择器

标题
```
>>> response.xpath('//div[@class="details"]/div[@class="article_title"]/h1/span/a/text()').extract()
```

链接
```
>>> response.xpath('//div[@class="details"]/div[@class="article_title"]/h1/span/a/@href').extract()
```

内容
```
>>> response.xpath('//div[@class="details"]/div[@class="article_content"]').extract()
```


## 增量抓取

[Jobs: 暂停，恢复爬虫](http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/jobs.html)

启用一个爬虫的持久化/恢复这个爬虫
```
✗ scrapy crawl somespider -s JOBDIR=crawls/somespider-1
```

安全的停止爬虫
```
Ctrl-C或者发送一个信号
```


## 框架介绍

### 架构概览

[架构概览-英文原版](http://scrapy.readthedocs.org/en/latest/topics/architecture.html)

[架构概览-中文翻译](http://scrapy-chs.readthedocs.org/zh_CN/latest/topics/architecture.html)

[数据流](http://scrapy.readthedocs.io/en/latest/topics/architecture.html#data-flow)

Scrapy的架构(时序：上、右、下、左)：

```
 ----------------------------------------------------------------------------------------
|                                  [调度器]
|                                (Scheduler)
|                                     |
|                                     |
|                                     |
|                                     |
|                                     |                    下载器
|[Item Pipeline] ------------- [Scrapy Engine] ----------- 中间件 ----------- [下载器]
|                                     |          (Downloader middlewares)  (Downloader)
|                                     |
|                                     |
|                               Spider中间件
|                           (Spider middlewares)
|                                     |
|                                     |
|                                     |
|                                 [Spiders]
 ----------------------------------------------------------------------------------------
```

### 组件介绍

[Scrapy Engine]
```
引擎负责控制数据流在系统中所有组件中流动，并在相应动作发生时触发事件。 
详细内容查看下面的数据流(Data Flow)部分。
```

[调度器(Scheduler)]
```
调度器从引擎接受request并将他们入队，以便之后引擎请求他们时提供给引擎。
```

[下载器(Downloader)]
```
下载器负责获取页面数据并提供给引擎，而后提供给spider。
```

[Spiders]
```
Spider是Scrapy用户编写用于分析response并提取item(即获取到的item)或额外跟进的URL的类。
每个spider负责处理一个特定(或一些)网站。
```

[Item Pipeline]
```
Item Pipeline负责处理被spider提取出来的item。
典型的处理有清理、 验证及持久化(例如存取到数据库中)。
当Item在Spider中被收集之后，它将会被传递到Item Pipeline，一些组件会按照一定的顺序执行对Item的处理
```

以下是item pipeline的一些典型应用：
```
清理HTML数据
验证爬取的数据(检查item包含某些字段)
查重(并丢弃)
将爬取结果保存到数据库中
```

[下载器中间件(Downloader middlewares)]
```
下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的response。
其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
```

[Spider中间件(Spider middlewares)]
```
Spider中间件是在引擎及Spider之间的特定钩子(specific hook)，处理spider的输入(response)和输出(items及requests)。
其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。更多内容请看 Spider中间件(Middleware) 。
```

更多可以参考[Scrapy实例演示](https://github.com/zhanghe06/scrapy_project)


## 调试

命令行调试
```
$ scrapy parse --spider=myspider -c parse_item -d 2 <item_url>

```

终端调试
```
from scrapy.shell import inspect_response

def parse_details(self, response):
    item = response.meta.get('item', None)
    if item:
        # populate more `item` fields
        return item
    else:
        inspect_response(response, self)
```


浏览器中显示
```
from scrapy.utils.response import open_in_browser

def parse_details(self, response):
    if "item name" not in response.body:
        open_in_browser(response)
```
