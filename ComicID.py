#遍历漫画

import urllib.request
import json
import csv
#import jsonpath


#获取json的函数：
def get_record(url):
    try:
        resp = urllib.request.urlopen(url)
        ele_json = json.loads(resp.read())
        return ele_json
    except Exception as e:
        print('漫画不存在!!!')
        # csv_writer.writerow([url + '漫画不存在!!!'])
if __name__ == '__main__':
    f = open('comic.csv','a',encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['id',"name","chapter","amount"])
    a = int(input("输入一个漫画id下限："))
    x = a
    b = int(input("输入一个漫画id上限: "))
    while x <= b :
        #url = 'http://v2.api.dmzj.com/comic/%d.json' % (x)
        #url = f'http://v3api.dmzj.com/comic/comic_{x}.json'
        url = f'http://v2.api.dmzj.com/comic/{x}.json'
        #改用字典操作
        comic = get_record(url)
        try:
            if type(comic) == dict and len(comic) != 0:
                comic_id = comic['id']
                comic_name = comic['title']
                comic_chapter = comic['chapters'][0]['data']
                print(comic_id,comic_name)
                for i in comic_chapter:
                    chapter_id = i['chapter_id']
                    url2 = f'http://v2.api.dmzj.com/chapter/{comic_id}/{chapter_id}.json'
                    #url2 = f'http://v3api.dmzj.com/chapter/{comic_id}/{chapter_id}.json'
                    chapter = get_record(url2)
                    print(chapter['title'],chapter['picnum'])
                    csv_writer.writerow([comic_id,comic_name,chapter['title'],chapter['picnum']])
                x += 1
            else:
                x += 1
        except Exception as e:
            print(str(comic_id) + 'is wrong!')
            x += 1
        continue

        #字典操作
        # if type(comic) == dict:
        #     print('id:',comic['id'])
        #     print('title:',comic['title'])
        #
        # x += 1

        #Jsonpath操作
        # try:
        #     id = jsonpath.jsonpath(get_record(url),'$.id')
        #     if(id == False):
        #         x += 1
        #     else:
        #         print('id:', id[0])
        #         title = jsonpath.jsonpath(get_record(url),'$.title')
        #         print('title:', title[0])
        #         x += 1
        # except Exception as e:
        #     pass
        # continue
