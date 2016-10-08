## Supervisor(Supervisor是一个进程监控程序)

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
```
[program:scrapyd]
process_name=%(program_name)s
command=scrapyd
directory=/Users/zhanghe/code/scrapy_project/app
startsecs=0
stopwaitsecs=0
autostart=true
autorestart=true
stdout_logfile=logs/scrapyd_out.log
stderr_logfile=logs/scrapyd_err.log
;environment=PATH="/Users/zhanghe/code/scrapy_project/scrapy.env/bin:%(ENV_PATH)s"
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
