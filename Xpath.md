
http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/selectors.html#xpaths

```
>>> divs = response.xpath('//div')
>>> lis = divs.xpath('.//li')
```


正则表达式提取数据
```
>>> from scrapy import Selector
>>> doc = """
... <div>
...     <ul>
...         <li class="item-0"><a href="link1.html">first item</a></li>
...         <li class="item-1"><a href="link2.html">second item</a></li>
...         <li class="item-inactive"><a href="link3.html">third item</a></li>
...         <li class="item-1"><a href="link4.html">fourth item</a></li>
...         <li class="item-0"><a href="link5.html">fifth item</a></li>
...     </ul>
... </div>
... """
>>> sel = Selector(text=doc, type="html")
>>> sel.xpath('//li[re:test(@class, "item-\d$")]//@href').extract_first()
u'link1.html'
```

获取页面源码

```
response.body  # 字节码
response.body_as_unicode()  # unicode 编码
```
