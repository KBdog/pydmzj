# pydmzj:简单获取动漫之家小说id的python程序
## About

因为动漫之家小说站已关闭，一些小说也无法通过搜索的api搜到，但是的确是存在的，于是遍历小说信息的api，从而获取所有小说的id信息。

```
小说详情
URL：http://v2.api.dmzj.com/novel/${id}.json
method: GET
content-type: text/html
params:
    id: 小说id
```

