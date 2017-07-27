# -*- coding:utf-8 -*-  
import urllib
import os
def save_pic(url,i) :
    save_path = '豆瓣图书图片'
    name = save_path + "/" + str(i) + ".jpg"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    url = "https://img3.doubanio.com/lpic/s1727290.jpg"
    conn = urllib.urlopen(url)
    f = open(name,'wb')
    f.write(conn.read())
    f.close()
