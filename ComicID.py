#遍历漫画

import urllib.request
import json

#获取json的函数：
def get_record(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json

if __name__ == '__main__':
    a = int(input("输入一个漫画id下限："))
    x = a
    b = int(input("输入一个漫画id上限: "))
    while x <= b :
        url = 'http://v2.api.dmzj.com/comic/%d.json' % (x)
        '''
            改用字典操作
        '''
        comic = get_record(url)
        if type(comic) == dict:
            print('id:',comic['id'])
            print('title:',comic['title'])
            print('author:',comic['authors'][0]['tag_name'])
        x += 1

    '''
        id = jsonpath.jsonpath(get_record(url),'$.id')
        if(id == False):
            x += 1
        else:
            print('id:', id[0])
            title = jsonpath.jsonpath(get_record(url),'$.tag_name')
            print('name:', title)
            x += 1
    '''