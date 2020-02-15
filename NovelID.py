#遍历小说
import urllib.request
import json
import jsonpath
#import pprint


#获取json的函数：
def get_record(url):
    resp = urllib.request.urlopen(url)
    ele_json = json.loads(resp.read())
    return ele_json

if __name__ == '__main__':
    a = int(input("输入一个小说id下限："))
    x = a
    b = int(input("输入一个小说id上限: "))
    ndir = []
    while x <= b :
        novelInfo = {}
        url = 'http://v2.api.dmzj.com/novel/%d.json' % (x)
        obj = get_record(url)
        #pprint.pprint(get_record(url))
        id = jsonpath.jsonpath(obj,'$.id')
        if(id == False):
            x += 1
        else:
            name = jsonpath.jsonpath(obj,'$.name')
            author = jsonpath.jsonpath(obj,'$.authors')
            # print('<tr>')
            # print('<td>{id}</td>'.format(id=id[0]))
            # print('<td>{name}</td>'.format(name = name[0]))
            # print('</tr>')
            print(id[0])
            novelInfo['id'] = id[0]
            novelInfo['name'] = name[0]
            novelInfo['authors'] = author[0]
            ndir.append(novelInfo)
            x += 1
    with open('novelist.json','a') as f:
        f.write(json.dumps(ndir,indent=4))