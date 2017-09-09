#user/bin/python3.6
import requests

def creatFile(file):
    fp = open(file,"w")
    return fp

def getHTMLText(url,file):
    try:
        kv = {'wd':'python'}
        res = requests.get(url, params = kv)
        print('URL: ' + res.request.url)
        print(res.status_code)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        print(res.text)
        file.write(str(res.text))
        file.close()
        return 'Ok'
    except Exception as err:
        print("error is ==>",err)
        return "Error"

if __name__ == "__main__":
    # url="https://www.lagou.com"
    url="https://www.baidu.com/s"
    index_file = "index.txt"
    file = creatFile(index_file)
    print(getHTMLText(url,file))
    