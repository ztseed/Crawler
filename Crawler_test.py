#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from http import cookiejar
import urllib3
import json  

urllib3.disable_warnings() 

url = "http://www.163.com"
http = urllib3.PoolManager()
response1 = http.request('GET', url)

print(response1.status)
# print(response1.data)

response_header = response1.info()               # 获取响应头
for key in response_header.keys():      # 循环遍历打印响应头信息
    print(key, ':', response_header.get(key))
