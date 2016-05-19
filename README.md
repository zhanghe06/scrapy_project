## Scrapy 项目实例

创建项目
```
$ scrapy startproject app
```

进入项目目录
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

