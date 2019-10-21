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

例如当id为2229的时候，Response:
```
{
"id": 2229,
"name": "从今天起我就是萝莉的小白脸！",
"zone": "\u65e5\u672c",
"status": "连载中",
"last_update_volume_name": "第一卷",
"last_update_chapter_name": "插画",
"last_update_volume_id": 8282,
"last_update_chapter_id": 68706,
"last_update_time": 1478948067,
"cover": "http:\/\/xs.dmzj.com\/img\/webpic\/3\/xbl1112l.jpg",
"hot_hits": 8473,
"introduction": "我——天堂晴悠哉地决定成为漫画家。有一天，我感觉自己的人生已经圆满了。那是因为，凭借投资赚得盆满钵满富得流油的美少女小学生——二条藤花居然是我的大粉丝，而且还说要成为我的赞助者！藤花让我住在她的家里，基本上不愁吃不愁穿，而且还给我买来各种各样的漫画BD手办Cos服装等能够成为我创作资料的东西！虽说有了资料也不一定能画出漫画，但既然有了如此梦幻般的环境，我总有一天一定能够画出名垂千古的作品的。……嗯，我想，大概可以吧……？充满甜蜜与快乐的理想小白脸生活，正式开始！",
"types": ["校园/后宫"],
"authors": "晓雪",
"subscribe_num": 5696,
"volume": [{
    "id": 8282,
    "lnovel_id": 2229,
    "volume_name": "第一卷",
    "volume_order": 10,
    "addtime": 1478947412,
    "sum_chapters": 9
}]
```
