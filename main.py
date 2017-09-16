#user/bin/python3.6
import requests
from bs4 import BeautifulSoup
import re

def creatFile(file):
    fp = open(file,"w")
    return fp

def getHTMLText(url,file):
    try:
        res = requests.get(url)
        print(res.status_code)
        res.raise_for_status()
        demo = res.text
        # print(demo)
        soup = BeautifulSoup(demo,'html.parser')
        print(soup.prettify())
        print('\n<=================================>\n')
        for tag in soup.find_all(id = re.compile('link')):
            print(tag)
        # file.write(soup.prettify())
        # file.close()
        return 'Ok' 
    except Exception as err:
        print("error is ==>",err)
        return 'Error'

if __name__ == "__main__":
    # url="https://www.lagou.com"
    url="http://python123.io/ws/demo.html"
    index_file = "index.txt"
    file = creatFile(index_file)
    print(getHTMLText(url,file))
    