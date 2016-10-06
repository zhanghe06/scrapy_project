## Scrapyd

Scrapyd is an application for deploying and running Scrapy spiders

[Scrapyd官方文档](http://scrapyd.readthedocs.org/en/latest/)

[scrapyd-client](https://github.com/scrapy/scrapyd-client)

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

项目中会产生一个文件 scrapy_project/app/app/twistd.pid
```
✗ cat app/twistd.pid
25673
✗ ps -aux | grep 25673
```

部署项目
```
$ scrapyd-deploy csdn_deploy -p csdn
Packing version 1442910194
Deploying to project "csdn" in http://localhost:6800/addversion.json
Server response (200):
{"status": "ok", "project": "csdn", "version": "1442910194", "spiders": 1, "node_name": "ubuntu"}
```

查看部署项目列表
```
$ scrapyd-deploy -l
csdn_deploy          http://localhost:6800/
```

查看具体部署项目
```
$ scrapyd-deploy -L csdn_deploy
default
csdn
```

查看项目列表
```
$ curl http://localhost:6800/listprojects.json
{"status": "ok", "projects": ["default", "csdn"], "node_name": "ubuntu"}
```

查看版本列表
```
$ curl http://localhost:6800/listversions.json?project=csdn
{"status": "ok", "versions": ["1442910194"], "node_name": "ubuntu"}
```

查看spider列表
```
$ curl http://localhost:6800/listspiders.json?project=csdn
{"status": "ok", "spiders": ["csdnblog"], "node_name": "ubuntu"}
```

调度新任务
```
$ curl http://localhost:6800/schedule.json -d project=csdn -d spider=csdnblog
{"status": "ok", "jobid": "6cf34b2e611011e59ff6000c29e23801", "node_name": "ubuntu"}
```

查看任务
```
$ curl http://localhost:6800/listjobs.json?project=csdn
{"status": "ok",
"running": [],
"finished": [
{"start_time": "2015-09-22 17:49:33.795207", "end_time": "2015-09-22 17:49:35.650616", "id": "38e5b66a610f11e59ff6000c29e23801", "spider": "csdnblog"},
{"start_time": "2015-09-22 17:50:08.796791", "end_time": "2015-09-22 17:50:10.791481", "id": "4ecfb4bc610f11e59ff6000c29e23801", "spider": "csdnblog"},
{"start_time": "2015-09-22 17:58:08.797639", "end_time": "2015-09-22 17:58:10.793856", "id": "6cf34b2e611011e59ff6000c29e23801", "spider": "csdnblog"}
],
"pending": [],
"node_name": "ubuntu"}
```

取消任务
```
$ curl http://localhost:6800/cancel.json -d project=csdn -d job=6cf34b2e611011e59ff6000c29e23801
```

删除项目
```
$ curl http://localhost:6800/delproject.json -d project=csdn
```
