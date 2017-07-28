# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib
from bs4 import  BeautifulSoup
import xlwt
import cv2
import time
import sys
import requests
reload(sys)
sys.setdefaultencoding("utf-8")

# PostUrl = 'http://passport.mysteel.com/login.jsp'
# cookie = cookielib.CookieJar()
# handler=urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://passport.mysteel.com/login.jsp')
#
#
# username = 'aad114314'
# password = '3825192'
#
# requestHeaders = {
# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'zh-CN,zh;q=0.8',
# 'Cache-Control':'max-age=0',
# 'Connection':'keep-alive',
# 'Content-Length':'105',
# 'Content-Type':'application/x-www-form-urlencoded',
# 'Cookie':cookie,
# 'Host':'passport.mysteel.com',
# 'Origin':'http://www.mysteel.com',
# 'Referer':'http://www.mysteel.com/',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
# }
#
# postData={
# 'my_username':'aad114314',
# 'my_password':'3825192',
# 'x':'22',
# 'y':'12',
# 'site':'mysteel',
# 'callback':'http://list1.mysteel.com/market/p-228-15480-----0--------1.html'
# }
# # cookie1 = cookielib.CookieJar()
# # handler1=urllib2.HTTPCookieProcessor(cookie1)
# # opener1 = urllib2.build_opener(handler1)
# # data = urllib.urlencode(postData)
# # request = urllib2.Request(PostUrl, data, requestHeaders)
# # response = opener1.open(request)
# # result = response.read()
# # for item in cookie1:
# #     print item.name+'='+item.value

url='http://jiancai.mysteel.com/m/16/1216/09/8369F5079653212C.html'
url1 = 'http://jiancai.mysteel.com/m/16/1214/10/777570070A604727.html'
def steel(title,url):
    dhead = {'cookie':'_login_token=4a89b3fbad4f6bbbc3eb918cbd27cbb1; _login_uid=8666; _login_mid=9317; _last_loginuname=aad114314; 4a89b3fbad4f6bbbc3eb918cbd27cbb1=35%3D10%2636%3D10%2615%3D10%2633%3D10%2616%3D10%2634%3D10%2613%3D10%2614%3D10%2637%3D10%2638%3D10%262%3D10%261%3D5%2642%3D10%2641%3D10%2632%3D10%264%3D10%2631%3D10%26catalog%3D010205%2C010202%2C0222%2C0223%2C0205; Hm_lvt_1c4432afacfa2301369a5625795031b8=1481597403,1481880582,1481895182; Hm_lpvt_1c4432afacfa2301369a5625795031b8=1481895633; jiathis_rdc=%7B%22http%3A//jiancai.mysteel.com/m/16/1216/09/8369F5079653212C.html%22%3A%2219%7C1481895633501%22%7D',
             'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    # req = urllib2.Request(url1, headers=dhead)
    # text = urllib2.urlopen(req).read()
    # # print text.decode('gbk')

    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('steel',cell_overwrite_ok=True)
    sheet.write(0,0,'品名')
    sheet.write(0,1,'规格')
    sheet.write(0,2,'材质')
    sheet.write(0,3,'产地')
    sheet.write(0,4,'价格')
    sheet.write(0,5,'涨跌')
    sheet.write(0,6,'备注')
    html = requests.get(url,headers=dhead).content
    html = html.decode('gbk')
    soup = BeautifulSoup(html,"lxml")

    # title = soup.find('title').getText("",strip=True)

    table = soup.find('table')
    i = 0
    for li in table.find_all('tr'):
        i+=1
        if i>=3:
            # td =li.getText("",strip=True)
            # print len(td)
            y = 0
            for td in li.find_all('td'):
                y+=1
                ttt = td.getText("",strip=True)
                if y==1:
                    print i,'品名',ttt

                if y==2:
                    print i,'规格',ttt
                if y==3:
                    print i,'材质',ttt
                if y==4:
                    print i,'产地',ttt
                if y==5:
                    print i,'价格',ttt
                sheet.write(i - 2, y - 1, ttt)
    book.save('E:\\steel\\'+title+'.xls')

steel('asd',url)




