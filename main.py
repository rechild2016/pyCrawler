#user/bin/python3.6
import requests

def creatFile(file):
    fp = open(file,"w")
    return fp

def getHTMLText(url,file):
    try:
        kv = {'User-Agent':'Mozilla/5.0'}
        res = requests.get(url, headers = kv)
        print(res.request.headers)
        print(res.status_code)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        print(res.text[1000:2000])
        file.write(str(res.text[1000:2000]))
        file.close()
        return 'Ok'
    except Exception as err:
        print("error is ==>",err)
        return "Error"

if __name__ == "__main__":
    # url="https://www.lagou.com"
    url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
    index_file = "index.txt"
    file = creatFile(index_file)
    print(getHTMLText(url,file))
    