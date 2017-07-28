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


def steel(name,url):
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

    title = soup.find('title').getText("",strip=True)

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
                # if y==1:
                #     print i,'品名',ttt
                #
                # if y==2:
                #     print i,'规格',ttt
                # if y==3:
                #     print i,'材质',ttt
                # if y==4:
                #     print i,'产地',ttt
                # if y==5:
                #     print i,'价格',ttt
                sheet.write(i - 2, y - 1, ttt)
    book.save('E://steel//'+name+'.xls')
    print name



urllist=[]
namelist = []
# url1 = 'http://list1.mysteel.com/market/p-228-15480-----0--------1.html'
def parse(url1):
    dhead1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    html1 = requests.get(url1, headers=dhead1).content
    html1 = html1.decode('gbk')
    soup1 = BeautifulSoup(html1, "lxml")
    list = soup1.find('ul',attrs={'class','nlist'})
    for a in list.find_all('li'):
        try:
            asd = a.find('a').get('href')
            nam = a.find('span').getText("", strip=True)
            steel(nam[0:13],asd)
        except:
            pass

    next_page = soup1.find('div', attrs={'class': 'page'}).find_all('a')
    return 'http://list1.mysteel.com'+next_page[-1].get('href')
for i in range(1,100):
    url1 = 'http://list1.mysteel.com/market/p-228-15480-----0--------'+str(i)+'.html'
    parse(url1)


