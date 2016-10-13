## Supervisor(Supervisor是一个进程监控程序)

http://supervisord.org/

进入虚拟环境(以下操作全部在虚拟环境进行)
```
✗ source scrapy.env/bin/activate
```

安装Supervisor
```
✗ pip install supervisor
```

生成配置文件(supervisord.conf)
```
✗ echo_supervisord_conf > etc/supervisord.conf
```

修改配置文件(etc/supervisord.conf)

虚拟环境
```
[program:scrapyd]
command=scrapyd
directory=/Users/zhanghe/code/scrapy_project/app
priority=200
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=logs/scrapyd.log


[group:crawl58]
programs=crawl58_banjia,crawl58_baojie,crawl58_baomu,crawl58_dianqi,crawl58_sjwx


[program:crawl58_banjia]
command=scrapy crawl crawl58_service_banjia_v4 -s JOBDIR=crawls/app/crawl58_service_banjia_v4
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=false


[program:crawl58_baojie]
command=scrapy crawl crawl58_service_baojie_v4 -s JOBDIR=crawls/app/crawl58_service_baojie_v4
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=false


[program:crawl58_baomu]
command=scrapy crawl crawl58_service_baomu_v4 -s JOBDIR=crawls/app/crawl58_service_baomu_v4
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=false


[program:crawl58_dianqi]
command=scrapy crawl crawl58_service_dianqi_v4 -s JOBDIR=crawls/app/crawl58_service_dianqi_v4
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=false


[program:crawl58_sjwx]
command=scrapy crawl crawl58_service_sjwx_v4 -s JOBDIR=crawls/app/crawl58_service_sjwx_v4
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=false
```

非虚拟环境
```
[program:scrapyd]
command=/Users/zhanghe/code/scrapy_project/scrapy.env/bin/scrapyd
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/Users/zhanghe/code/scrapy_project/app/logs/scrapyd.log
```


开启守护
```
✗ source scrapy.env/bin/activate
✗ supervisord                       # 配置默认目录 包含etc/supervisord.conf
```

默认 tmp 目录会生成以下3个文件
```
✗ ll | grep supervisor
srwx------  1 zhanghe  wheel     0B 10  8 13:34 supervisor.sock
-rw-r--r--  1 zhanghe  wheel   789B 10  8 13:34 supervisord.log
-rw-r--r--  1 zhanghe  wheel     6B 10  8 13:34 supervisord.pid
```

加载配置 重启守护进程
```
✗ supervisorctl reload
✗ supervisorctl restart all
```

supervisord.conf 配置文件默认搜索顺序
```
$CWD/supervisord.conf
$CWD/etc/supervisord.conf
/etc/supervisord.conf
/etc/supervisor/supervisord.conf (since Supervisor 3.3.0)
../etc/supervisord.conf (Relative to the executable)
../supervisord.conf (Relative to the executable)
```


## Mac 下全局安装的坑

```
✗ pip install supervisor
✗ echo_supervisord_conf > /etc/supervisord.conf
```
会提示：permission denied: /etc/supervisord.conf

解决办法：
```
✗ cd ~
✗ echo_supervisord_conf > supervisord.conf
✗ sudo mv supervisord.conf /etc/supervisord.conf
```
然后就可以编辑了
```
✗ vim /etc/supervisord.conf
```

通过 supervisorctl 查看 supervisor 状态
```
✗ supervisorctl status
```


## 备注

("~" or "$HOME") is not supported.  Environment

日志记录
```
autorestart=true
redirect_stderr=true
```
或者
```
stdout_logfile=logs/scrapyd_out.log
stderr_logfile=logs/scrapyd_err.log
```


```
priority=999
;进程启动关闭优先级，优先级低的，最先启动，关闭的时候最后关闭 默认值为 999 非必须设置

autostart=true
;如果是 true 的话，子进程将在 supervisord 启动后被自动启动 默认就是 true 非必须设置
```


## 管理分组

组名后面加:（半角冒号）

```
✗ supervisorctl start crawl58:
crawl58:crawl58_banjia           RUNNING   pid 13195, uptime 0:00:05
crawl58:crawl58_baojie           RUNNING   pid 13197, uptime 0:00:05
crawl58:crawl58_baomu            RUNNING   pid 13194, uptime 0:00:05
crawl58:crawl58_dianqi           RUNNING   pid 13198, uptime 0:00:05
crawl58:crawl58_sjwx             RUNNING   pid 13196, uptime 0:00:05
scrapyd                          RUNNING   pid 13152, uptime 0:03:25
✗ supervisorctl stop crawl58:
✗ supervisorctl status
crawl58:crawl58_banjia           STOPPED   Oct 13 08:15 PM
crawl58:crawl58_baojie           STOPPED   Oct 13 08:15 PM
crawl58:crawl58_baomu            STOPPED   Oct 13 08:15 PM
crawl58:crawl58_dianqi           STOPPED   Oct 13 08:15 PM
crawl58:crawl58_sjwx             STOPPED   Oct 13 08:15 PM
scrapyd                          RUNNING   pid 13152, uptime 0:03:37
```
