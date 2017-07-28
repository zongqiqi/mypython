# -*- coding: utf8 -*-


def ancaiwangzhan():
    import urllib2
    import urllib
    import cookielib
    import cv2
    import time
    import sys
    # cookie = cookielib.CookieJar()
    # handler=urllib2.HTTPCookieProcessor(cookie)
    # opener = urllib2.build_opener(handler)
    # response = opener.open('http://211.86.241.171/loginAction.do')

    reload(sys)
    sys.setdefaultencoding("utf-8")

    CaptchaUrl = 'http://211.86.241.171/validateCodeAction.do?random=0.3765381710860165'
    PostUrl = 'http://211.86.241.171/loginAction.do'
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)

    username = '20132273'
    password = 'QNYDMD'
    picture = opener.open(CaptchaUrl).read()
    local = open('image.jpg', 'wb')
    local.write(picture)
    local.close()
    v_yzm = raw_input('输入验证码： ')
    postData = {
    'zjh1':'',
    'tips':'',
    'lx':'',
    'evalue':'',
    'eflag':'',
    'fs':'',
    'dzslh':'',
    'zjh':username,
    'mm':password,
    'v_yzm':v_yzm
    }
    for item in cookie:
        cookie1 = item.name+'='+item.value
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'75',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':cookie1,
    'Host':'211.86.241.171',
    'Origin':'http://211.86.241.171',
    'Referer':'http//211.86.241.171/logout.do',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }

    URL2 = 'http://211.86.241.171/outlineAction.do'
    data = urllib.urlencode(postData)
    request = urllib2.Request(PostUrl, data,headers)
    response = opener.open(request)
    result = response.read()

    headers2 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':cookie1,
    'Host':'211.86.241.171',
    'Referer':'http://211.86.241.171/menu/menu.jsp',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }

    request2 = urllib2.Request(url=URL2,headers=headers2)
    response2 = opener.open(request2)
    result2 = response2.read()


    URL3 = 'http://211.86.241.171/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2015-2016%D1%A7%C4%EA%B4%BA(%C1%BD%D1%A7%C6%DA)'
    headers3 = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':cookie1,
    'Host':'211.86.241.171',
    'Referer':'http://211.86.241.171/gradeLnAllAction.do?type=ln&oper=qb',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }

    request3 = urllib2.Request(url=URL3,headers=headers3)
    response3 = opener.open(request3)
    result3 = response3.read()


    print result
    print result2
    print result3
    print cookie1

aaa = ancaiwangzhan()

