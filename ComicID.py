#遍历漫画

import urllib.request
import json
import jsonpath
import time

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
        print(get_record(url))
        #改用字典操作
        '''
        若用jsonpath操作，将下面未注释的注释即可，然后将注释的取消注释。
        测试的dict操作比jsonpath效率高一点。
        '''
        comic = get_record(url)
        if type(comic) == dict:
            print('id:',comic['id'])
            print('title:',comic['title'])
            print('author:',comic['authors'][0]['tag_name'])
        x += 1

        #Jsonpath操作
        '''
        id = jsonpath.jsonpath(get_record(url),'$.id')
        if(id == False):
            x += 1
        else:
            print('id:', id[0])
            title = jsonpath.jsonpath(get_record(url),'$.title')
            print('title:', title[0])
            author = jsonpath.jsonpath(get_record(url),'$.authors..tag_name')
            print('author:', author[0])
            x += 1
        '''
