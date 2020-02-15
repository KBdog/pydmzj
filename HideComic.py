# 遍历漫画隐藏
# 多线程处理数据

import urllib.request
import json
import threading

# 创建线程类


class myThread (threading.Thread):
    def __init__(self, threadID, name, list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.list = list

    def run(self):
        print ("开始线程：" + self.name)
        get_id(self.name, self.list)
        print ("退出线程：" + self.name)


# 请求url
def get_record(url):
    try:
        resp = urllib.request.urlopen(url)
        ele_json = json.loads(resp.read())
        return ele_json
    except Exception as e:
        return "漫画不存在！"


# 获取数据
def get_id(threadName, cid):
    li = []
    for i in cid:
        url = f'http://v2.api.dmzj.com/comic/{i}.json'
        comic = get_record(url)
        if (comic == "漫画不存在！"):
            # print(threadName + ':comic_id: ' +  str(i))
            li.append(i)
    if(len(li) != 0):
        print(li)


# 平分要处理的数组
def split_list_n_list(origin_list, n):
    if len(origin_list) % n == 0:
        cnt = len(origin_list) // n
    else:
        cnt = len(origin_list) // n + 1

    for i in range(0, n):
        yield origin_list[i * cnt:(i + 1) * cnt]


def tHideComic(low, up, n):
    li = []
    for i in range(low, up+1):
        li.append(i)
    # print(li)
    split_li = split_list_n_list(li, n)
    counter = 1
    for i in split_li:
        tname = f'thread{counter}'
        cid = tuple(i)
        # print(cid)
        myThread(counter, tname, cid).start()
        counter += 1


if __name__ == '__main__':
    tHideComic(10000,15000,12)
