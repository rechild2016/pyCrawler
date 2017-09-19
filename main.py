#coding=utf-8
#user/bin/python3.6
import requests
from bs4 import BeautifulSoup
import bs4
import re
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def creatFile(file):
    fp = open(file,"w")
    return fp

def getHTMLText(url):
    try:
        res = requests.get(url, timeout = 20)
        print(res.status_code)
        res.raise_for_status()
        res.encoding=res.apparent_encoding
        demo = res.text
        return demo
    except Exception as err:
        print("error is ==>",err)
        return 'Error'

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format(u"排名", u"学校",u"省份",chr(12288)))
    for i in range(num):
        item=ulist[i]
        print(tplt.format(item[0], item[1], item[2],chr(12288)))
if __name__ == "__main__":
    # url="https://www.lagou.com"
    url="http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    index_file = "index.txt"
    uinfo = []
    # file = creatFile(index_file)
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
