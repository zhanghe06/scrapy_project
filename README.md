## Scrapy 项目实例

创建项目
```
$ scrapy startproject app
```

进入项目根目录（scrapy.cfg 存放的目录被认为是 项目的根目录 ）
```
$ cd app
```

创建一个新的spider（蜘蛛）
```
$ scrapy genspider local_test localhost:5000
```

设计蜘蛛程序...

使用刚刚创建的spider进行爬取
```
$ scrapy crawl local_test
```

关于缓存
```
开启之后，不会重新请求被缓存的页面，提示如下：
DEBUG: Crawled (200) <GET http://localhost:5000/blog/list/> (referer: None) ['cached']
```

如果需要更新抓取结果，则需要清空缓存


## 数据处理

sqlalchemy

```
$ pip install MySQL-python
$ pip install SQLAlchemy
$ pip install sqlacodegen
```
[http://doc.scrapy.org/en/latest/topics/item-pipeline.html](http://doc.scrapy.org/en/latest/topics/item-pipeline.html)


## 页面处理
[http://doc.scrapy.org/en/latest/topics/selectors.html](http://doc.scrapy.org/en/latest/topics/selectors.html)


## Request 优先级
[http://doc.scrapy.org/en/latest/topics/request-response.html?highlight=priority#request-objects](http://doc.scrapy.org/en/latest/topics/request-response.html?highlight=priority#request-objects)

priority (int) – the priority of this request (defaults to 0).
The priority is used by the scheduler to define the order used to process requests.
Requests with a higher priority value will execute earlier.
Negative values are allowed in order to indicate relatively low-priority.

默认为0, 值越高优先级越大, 允许为负值


## Pipeline 优先级
[Item Pipeline](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)

The integer values you assign to classes in this setting determine the order in which they run: 
items go through from lower valued to higher valued classes.
It’s customary to define these numbers in the 0-1000 range.

顺序由低到高的执行, 值越小, 先执行, 通常取值范围(0-1000)


## Settings 配置

参考 [Settings](http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/settings.html)

RANDOMIZE_DOWNLOAD_DELAY = True     # 默认 True（0.5 到 1.5 之间的一个随机值 * DOWNLOAD_DELAY）

DOWNLOAD_DELAY = 0.25               # 250 ms of delay 设置为正数, 支持小数（默认 0）

ROBOTSTXT_OBEY = False              # 默认 False（如果启用, Scrapy 将会尊重 robots.txt 策略）

DEFAULT_REQUEST_HEADERS             # 将配置的注释打开即可

COOKIES_ENABLED = False             # 禁用cookie 默认是开启的, 注释打开即可
