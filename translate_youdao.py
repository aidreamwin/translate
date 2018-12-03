
# coding: utf-8

# ## 有道翻译
# 
# 通过读取文件中的内容来翻译文档，逐行翻译。

# In[ ]:


#/usr/bin/python 

# __Author__ = Slwhy

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import requests
import time
import random
import hashlib
import json

def translate(input_data):
    salt = str(int(time.time()*1000)+random.randint(1,10))
#     input_data = raw_input("please input the word you want to translate:")
    u = 'fanyideskweb'
    c = 'aNPG!!u6sesA>hBAW1@(-'
    src = u + input_data + salt + c    # u 与 l 是固定字符串，t是你要翻译的字符串，i是之前的时间戳
    m1 = hashlib.md5()
    m1.update(src)
    sign = m1.hexdigest()

    head = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Content-Length':'200',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',    
    }
    head['Cookie'] = 'OUTFOX_SEARCH_USER_ID=833904829@10.169.0.84;                         OUTFOX_SEARCH_USER_ID_NCOO=1846816080.1245883;                          ___rl__test__cookies='+str(time.time()*1000)


    data = {
        'i': input_data,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false'
    }

    s = requests.session()
    # print data
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    p = s.post(url,data= data,headers = head)
    return p


# print p.text

def start(file_name):
    with open(file_name,"r") as f:
        input_data = f.read()
        input_data = input_data.replace("\n"," ")
    x = translate(input_data)
    data = x.text

    data_json = json.loads(data)
    # print(data_json)

    translateResult = data_json["translateResult"][0]
    # print(translateResult)

    print("\n")

    for dict_x in translateResult:
        for index,value in dict_x.items():
            print(value)
    print("\n")        
    for dict_x in translateResult:
        print(dict_x["tgt"])


# In[ ]:


start("input.txt")

