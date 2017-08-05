import requests
import json

url="https://api.shanbay.com/account/"

r=requests.get(url=url)
contents=r.text
print(contents)
s=json.loads(contents)
# print(s.keys())
# print(s['msg'])