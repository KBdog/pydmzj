#对json的一系列操作
import urllib.request
import json

#获取json的函数：
def get_record(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json

url = 'http://v2.api.dmzj.com/comic/44516.json'
'''
以44516.json文件为例：get_record(url)获得的是这样的文件：
{
 'id': 44516,
 'islong': 2, 
 'direction': 1, 
 'title': '只有我进入的隐藏地下城～悄悄锻炼成为世界最强～', 
 'is_dmzj': 0, 
 'cover': 'https://images.dmzj.com/webpic/11/004zhiyouwoengjinrudxc233705.jpg', 
 'description': '最强新连载开幕！', 
 'last_updatetime': 1569943355, 
 'copyright': 0, 
 'first_letter': 'z', 
 'hot_num': 28111172, 
 'hit_num': 5423297, 
 'uid': None, 
 'types': [{'tag_id': 4, 'tag_name': '冒险'}, {'tag_id': 6316, 'tag_name': '轻小说'}], 
 'status': [{'tag_id': 2309, 'tag_name': '连载中'}], 
 'authors': [{'tag_id': 11919, 'tag_name': '樋野友行'}, {'tag_id': 15055, 'tag_name': '濑户メグル'}], 
 'subscribe_num': 130069, 
} 
整理一下可以看出最外层是个字典{}，可以根据字典的查找来获取想要的内容
'''
#获取id:
Test = get_record(url)
print(Test['id'])
#获取title:
print(Test['title'])
#获取作者：
print(Test['authors'])
'''
获取作者的时候返回了一个列表，也就是对Test查找'authors'键的值为一个列表:
[{'tag_id': 11919, 'tag_name': '樋野友行'}, {'tag_id': 15055, 'tag_name': '濑户メグル'}]
也就是Test['authors']是一个列表，而中的每一项又是一个字典，那么我们只获取我们需要的每一项的tag_name只要遍历Test['authors']列表
然后对每一项再进行字典的查找，查找'tag_name'的值即可

'''
for i in Test['authors']:
    print(i['tag_name'])

'''
综上，通过列表和字典的操作，就能把自己想要的内容提取出来了。
'''