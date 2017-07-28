# -*- coding: utf-8 -*-

#Request URL_1 = http://www.kuaidi100.com/query?type=debangwuliu&postid=884238800992987778&id=1&valicode=&temp=0.13838365224428828
#{"message":"快递公司参数异常：单号不存在或者已经过期","nu":"884238800992987778","ischeck":"0","condition":"","com":"debangwuliu","status":"201","state":"0","data":[]}

#Request URL_2 = http://www.kuaidi100.com/query?type=yuantong&postid=884238800992987778&id=1&valicode=&temp=0.960708810646951
#{"message":"ok","nu":"884238800992987778","ischeck":"1","condition":"F00","com":"yuantong","status":"200","state":"3","data":[{"time":"2017-02-18 19:15:31","ftime":"2017-02-18 19:15:31","context":"客户 签收人: 北苑三栋菜鸟驿站签收 已签收 感谢使用圆通速递，期待再次为您服务","location":""},{"time":"2017-02-18 11:40:14","ftime":"2017-02-18 11:40:14","context":"【安徽省蚌埠市大学城二部公司】 派件人: 贾梅 派件中 派件员电话13275523399","location":""},{"time":"2017-02-18 08:02:18","ftime":"2017-02-18 08:02:18","context":"【安徽省蚌埠市公司】 已发出 下一站 【安徽省蚌埠市大学城二部公司】","location":""},{"time":"2017-02-17 14:20:09","ftime":"2017-02-17 14:20:09","context":"【蚌埠转运中心】 已发出 下一站 【安徽省蚌埠市公司】","location":""},{"time":"2017-02-17 14:15:46","ftime":"2017-02-17 14:15:46","context":"【蚌埠转运中心】 已收入","location":""},{"time":"2017-02-16 23:10:15","ftime":"2017-02-16 23:10:15","context":"【温州转运中心】 已发出 下一站 【蚌埠转运中心】","location":""},{"time":"2017-02-16 23:07:32","ftime":"2017-02-16 23:07:32","context":"【温州转运中心】 已收入","location":""},{"time":"2017-02-16 21:20:25","ftime":"2017-02-16 21:20:25","context":"【浙江省温州市永嘉县瓯北一部公司】 已发出 下一站 【温州转运中心】","location":""},{"time":"2017-02-16 20:57:49","ftime":"2017-02-16 20:57:49","context":"【浙江省温州市永嘉县瓯北一部公司】 已打包","location":""},{"time":"2017-02-16 19:23:55","ftime":"2017-02-16 19:23:55","context":"【浙江省温州市永嘉县瓯北一部公司】 已收件","location":""}]}

import urllib2
import json
import time

# url = "http://www.kuaidi100.com/query?type=yuantong&postid=884238800992987778&id=1&valicode="
# req = urllib2.Request(url)
# response = urllib2.urlopen(req)
# content = response.read()
# print content
# content = json.loads(content)
# print content["status"]

for a1 in xrange(10):
    for a2 in xrange(10):
        for a3 in xrange(10):
            for a4 in xrange(10):
                for a5 in xrange(10):
                    for a6 in xrange(10):
                        for a7 in xrange(10):
                            for a8 in xrange(10):
                                a = "%d"%a1+"%d"%a2+"%d"%a3+"%d"%a4+"%d"%a5+"%d"%a6+"%d"%a7+"%d"%a8
                                print a
                                time.sleep(1)




