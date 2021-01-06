import socket

import requests
from bs4 import BeautifulSoup
socket.setdefaulttimeout(20)
# 请求头
headers1 = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
}

with open("url.txt") as fd:
    count = 0
    while True:
        fw = open("C:/Users/123/PycharmProjects/Text_Summarization/data/"+str(count)+".txt", "w", encoding="utf-8")
        line = fd.readline()
        if not line:
            break
        line = line.strip()
        r1 = requests.get(line, headers=headers1)
        bs = BeautifulSoup(r1.text, "html.parser")
        title = bs.title.get_text()
        title = title[:-5]
        fw.write(title+"\n")
        p = bs.find_all("p")
        for i in p:
            fw.write(i.get_text())
        count = count + 1
        print(title)
        print(str(count)+".txt")
