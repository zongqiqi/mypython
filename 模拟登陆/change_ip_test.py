#-*- coding:utf-8 -*-

url1='http://127.0.0.1:8000/?types=0&count=5&country=国内'

import requests
import json
r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内')
ip_ports = json.loads(r.text)
print ip_ports
ip = ip_ports[0][0]
port = ip_ports[0][1]
proxies={
    'http':'http://%s:%s'%(ip,port),
    'https':'http://%s:%s'%(ip,port)
}
r = requests.get('http://4xqn5l.v.tp8.me/Front/Ajax/GetVote.ashx?VoteChannel=MobileWeb&OptionID=6557173&TimeStamp=1495177288%2C7be02c051ac0d6e88c7d3cb9207652f3&RefererUrl=http%3A%2F%2F4xqn5l.v.tp8.me%2Fm',proxies=proxies)
r.encoding='utf-8'
print r.text