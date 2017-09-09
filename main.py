#user/bin/python3.6
import requests

def creatFile(file):
    fp = open(file,"wb")
    return fp

def getHTMLText(url,file):
    try:
        res = requests.get(url)
        print('URL: ' + res.request.url)
        print(res.status_code)
        res.raise_for_status()
        file.write(res.content)
        file.close()
        return 'Ok'
    except Exception as err:
        print("error is ==>",err)
        return "Error"

if __name__ == "__main__":
    # url="https://www.lagou.com"
    url="http://img06.tooopen.com/images/20160921/tooopen_sy_179583447187.jpg"
    index_file = "index.jpg"
    file = creatFile(index_file)
    print(getHTMLText(url,file))
    