# -*- coding: utf-8 -*
import requests
from lxml import etree
import time
import random
import socket
import json

socket.setdefaulttimeout(20)
# 请求头
headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Proxy-Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
}

# 代理
proxy_list = [
    {"https": "218.60.8.98:3129"},
    {"https": "218.60.8.83:3129"},
    {"https": "218.60.8.99:3129"}
]

# 获取所有 li标签
xpath_items = '//ul[@class="note-list"]/li'
# 对每个 li标签再提取
xpath_link = './div/a/@href'
xpath_title = './div/a[@class="title"]/text()'
xpath_abstract = './div/p/text()'

a = 'added_at'
count = 1
# 获取和解析网页
num = 0
f = open("url.txt", "w", encoding="utf-8")
while count < 201:
    proxy = random.choice(proxy_list)
    print(proxy)
    r1 = requests.get('https://www.jianshu.com/c/b591324d6443?order_by={}&page={}'.format(a, count), headers=headers1)
    print('https://www.jianshu.com/c/b591324d6443?order_by={}&page={}'.format(a, count))
    r1.encoding = r1.apparent_encoding
    dom1 = etree.HTML(r1.text)
    print(r1.status_code)
    filename = "numbers.json"

    # 获取所有的文章标签
    items1 = dom1.xpath(xpath_items)
    for article in items1:
        t = {}
        t['link'] = 'https://www.jianshu.com' + article.xpath(xpath_link)[0]
        t['title'] = article.xpath(xpath_title)[0]
        print(t)
        f.write(t['link']+"\n")
    # 解析完毕
    count = count + 1
    print(count)
    r1.close()
    s = random.randint(1, 10)
    time.sleep(s)
f.close()
