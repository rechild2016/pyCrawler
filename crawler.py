#coding=utf-8
#user/bin/python3.6
import requests
from bs4 import BeautifulSoup
import bs4
# import re
import string
import io
import sys
import pymysql
import codecs
from urllib.parse import urlparse
from urllib.parse import urljoin

#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def getHTMLText(url,page):
    try:
        url = url.format(page = page)
        res = requests.get(url, timeout = 20)
        print(res.status_code)
        # res.raise_for_status()
        # res.encoding=res.apparent_encoding
        demo = res.text
        return demo
    except Exception as err:
        print("error is ==>",err)
        return 'Error'

def getRentingInfo(text):
    html = BeautifulSoup(text,'html.parser')
    house_list = html.select(".list > li")
    return house_list


url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"

# Open database connection
db = pymysql.connect("localhost","root","lijie110","test_schema" )
# prepare a cursor object using cursor() method
cursor = db.cursor()


text = getHTMLText(url,0)
house_list = getRentingInfo(text)

for house in house_list:
    mydivs = house.findAll("p",{ "class" : "room" })
    # print(mydivs)
    for div in mydivs:
        for child in div.children:
            if(child.string != "\n"):
                s = str(child.string)
                s1 = " ".join(s.split())
                print (s1,type(s1))
                try:
                    cursor.execute("""INSERT INTO test_schema.info(it) VALUES (%s)""",(s1.encode('utf-8')))
                    db.commit()
                    print("-----------------------")
                except:
                    db.rollback()
                
    print("====================================\n")

db.close()