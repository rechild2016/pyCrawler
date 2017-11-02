#coding=utf-8
#user/bin/python3.6
import requests
from bs4 import BeautifulSoup
import bs4
import re
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
        res = requests.get(url, timeout = 80)
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

def getHouseInfo(house):
    house_title = house.select("h2")[0].string
    house_url = urljoin(url, house.select("a")[0]["href"])
    house_id = house.select("a")[0]["href"].split(".shtml")[0]
    room = house.select(".room")[0]
    s="".join(str(room).split())
    result=re.findall(r">(.*)<",s)[0]   #"1室1厅1卫20m²朝东<b>可短租</b>"
    roominfo = result.split("<b>")[0]
    
    house_money = house.select(".money")[0].select("b")[0].string
    houseInfo={"title":house_title,"url":house_url,"room":roominfo,
                "money":house_money,"id":house_id}
    return houseInfo

url = "http://nj.58.com/pinpaigongyu/pn/{page}/?"

# Open database connection
db = pymysql.connect("localhost","root","lijie110","test_schema" )
# prepare a cursor object using cursor() method
cursor = db.cursor()


text = getHTMLText(url,0)
house_list = getRentingInfo(text)

houseInfos=[]
for house in house_list:
    infodir = getHouseInfo(house)
    houseInfos.append(infodir)
   
    # try:
    #     cursor.execute("""INSERT INTO test_schema.info(it) VALUES (%s)""",(s1.encode('utf-8')))
    #     db.commit()
    #     print("-----------------------")
    # except:
    #     db.rollback()
    print(infodir,'\n')

db.close()