#user/bin/python3.6
import requests

def creatFile(file):
    fp = open(file,"w")
    return fp

def getHTMLText(url,file):
    try:
        res = requests.get(url)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        file.write(res.text)
        file.close()
        return 'Ok'
    except Exception as err:
        print("error is ==>",err)
        return "Error"


if __name__ == "__main__":
    url="https://www.lagou.com"
    index_file = "index.txt"
    file = creatFile(index_file)
    print(getHTMLText(url,file))
    