创建测试库
```
✗ psql -U postgres -d test -f pg.sql
```

部署
```
curl http://localhost:6800/schedule.json -d project=app -d spider=crawl58
curl http://localhost:6800/schedule.json -d project=app -d spider=crawl58v2
```
