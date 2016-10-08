## Scrapyd

Scrapyd is an application for deploying and running Scrapy spiders

[Scrapyd官方文档](http://scrapyd.readthedocs.org/en/latest/)

[scrapyd-client](https://github.com/scrapy/scrapyd-client)

进入项目目录(重要)
```
✗ cd app
```
scrapyd scrapyd-deploy 所有操作都需要在项目目录下进行

开启Scrapyd
```
✗ scrapyd
2016-10-07 01:04:51+0800 [-] Log opened.
2016-10-07 01:04:51+0800 [-] twistd 15.4.0 (/home/zhanghe/code/scrapy_project/scrapy.env/bin/python 2.7.6) starting up.
2016-10-07 01:04:51+0800 [-] reactor class: twisted.internet.epollreactor.EPollReactor.
2016-10-07 01:04:51+0800 [-] Site starting on 6800
2016-10-07 01:04:51+0800 [-] Starting factory <twisted.web.server.Site instance at 0x7f96189c7fc8>
2016-10-07 01:04:51+0800 [Launcher] Scrapyd 1.1.0 started: max_proc=16, runner='scrapyd.runner'
```

项目中会产生一个文件 twistd.pid（scrapyd的进程id）
```
✗ cat twistd.pid
25673
✗ ps -aux | grep 25673
```

添加部署配置

app/scrapy.cfg
```
[deploy:app]
url = http://localhost:6800/
project = app
```

部署项目
```
✗ scrapyd-deploy app -p app
Packing version 1475896129
Deploying to project "app" in http://localhost:6800/addversion.json
Server response (200):
{"status": "ok", "project": "app", "version": "1475896129", "spiders": 4, "node_name": "zhanghedeMacBook-Pro.local"}
```

部署完成，项目目录（app）会新增以下目录（需要忽略版本控制的跟踪，添加到.gitignore中）
```
build/
dbs/
eggs/
project.egg-info/
setup.py
twistd.pid
```

查看部署项目列表
```
✗ scrapyd-deploy -l
app                  http://localhost:6800/
```

查看具体部署项目
```
✗ scrapyd-deploy -L app
default
app
```

查看项目列表
```
✗ curl http://localhost:6800/listprojects.json
{"status": "ok", "projects": ["default", "app"], "node_name": "zhanghedeMacBook-Pro.local"}
```

查看版本列表
```
✗ curl http://localhost:6800/listversions.json?project=app
{"status": "ok", "versions": ["1475896129"], "node_name": "zhanghedeMacBook-Pro.local"}
```

查看spider列表
```
✗ curl http://localhost:6800/listspiders.json?project=app
{"status": "ok", "spiders": ["crawl58", "ip", "local_test", "wealink"], "node_name": "zhanghedeMacBook-Pro.local"}
```

调度新任务
```
✗ curl http://localhost:6800/schedule.json -d project=app -d spider=crawl58
{"status": "ok", "jobid": "6cf34b2e611011e59ff6000c29e23801", "node_name": "zhanghedeMacBook-Pro.local"}
```

查看任务
```
✗ curl http://localhost:6800/listjobs.json?project=app
{"status": "ok",
"running": [],
"finished": [
{"start_time": "2015-09-22 17:49:33.795207", "end_time": "2015-09-22 17:49:35.650616", "id": "38e5b66a610f11e59ff6000c29e23801", "spider": "crawl58"},
{"start_time": "2015-09-22 17:50:08.796791", "end_time": "2015-09-22 17:50:10.791481", "id": "4ecfb4bc610f11e59ff6000c29e23801", "spider": "crawl58"},
{"start_time": "2015-09-22 17:58:08.797639", "end_time": "2015-09-22 17:58:10.793856", "id": "6cf34b2e611011e59ff6000c29e23801", "spider": "crawl58"}
],
"pending": [],
"node_name": "zhanghedeMacBook-Pro.local"}
```

取消任务
```
✗ curl http://localhost:6800/cancel.json -d project=app -d job=6cf34b2e611011e59ff6000c29e23801
```

删除项目
```
✗ curl http://localhost:6800/delproject.json -d project=app
```
