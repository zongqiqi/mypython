import time
"""格式化时间输出，并暂停一秒
网址：http://www.cnblogs.com/vipitsoft/p/5628993.html
"""
time1 = time.strftime('%Y-%m-%d  %X',time.localtime(time.time()))
print (time1)
time.sleep(1)
time2 = time.strftime('%Y-%m-%d  %X',time.localtime(time.time()))
print (time2)


