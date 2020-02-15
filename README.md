# pydmzj:简单获取动漫之家小说id的python程序
## About

因为动漫之家小说站已关闭，一些小说也无法通过搜索的api搜到，但是的确是存在的，于是遍历小说信息的api，从而获取所有小说的id信息。

```
此API通过Charles抓包获得,未进行任何破解。此API仅供开发研究使用,API使用者造成的一切侵犯动漫之家权益的行为,请使用者自行承担责任。   
小说详情api:  
http://v2.api.dmzj.com/novel/${id}.json (旧)  
http://v3api.dmzj.com/novel/${id}.json (新)  
漫画详情api:  
http://v2.api.dmzj.com/comic/${id}.json (旧)  
http://v3api.dmzj.com/comic/comic_${id}.json(新)  
漫画下载api:  
https://imgzip.dmzj.com/${first_character/number}/${comic_id}}/${chapter_id}.zip  
其中  
${first_character/number}：漫画名称首字母或者数字  
${comic_id}:漫画id  
${chapter_id}:章节id  
漫画章节信息api:  
http://v3api.dmzj.com/chapter/${comic_id}/${chapter_id}.json  
漫画章节吐槽api:
http://v3api.dmzj.com/viewPoint/0/${comic_id}/${chapter_id}.json  
```


## NovelID.py

逻辑很简单，遍历给定id上下限之间的所有漫画信息，打印出其中的id和name信息，用于更新另一仓库里的dmzjxsid.txt文件，方便手机端检索以及跳转操作。

## ComicID.py
遍历所有漫画的信息，打印出id和title。  
现在动漫之家下架了一些隐藏漫画，相应链接返回的并不是字符串，从url获取json会出错。通过直接读取网页内容即可。或者写个抛出继续运行，忽略错误的url.

## HideComic.py
多线程处理获取隐藏漫画id...