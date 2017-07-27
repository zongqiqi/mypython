# -*- coding: utf-8 -*-

import logging
import urllib2
import json
import time
import datetime
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def get_token():
    apiKey = "PVqFNkGZ3H3GYGllkYbGACGW"
    secretKey = "b65d566a821cf624febc8fde5fbc3595"

    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;

    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    #    print 'json_data:',type(json_data)
    return json.loads(json_data)['access_token']


def playaudio(file_path):
    import pymedia.muxer as muxer
    import pymedia.audio.acodec as acodec
    import pymedia.audio.sound as sound
    import os.path as path
    root, ext = path.splitext(file_path)
    demuxer = muxer.Demuxer(ext[1:].lower())
    decoder = None
    output = None

    file = open(file_path, 'rb')
    data = ' '
    while data:
        data = file.read(20000)
        if len(data) < 20000 and len(data) > 0:
            data = data + ' ' * 20000
        if len(data):
            frames = demuxer.parse(data)
            # print len(frames)
            for frame in frames:
                if decoder == None:
                    decoder = acodec.Decoder(demuxer.streams[0])

                audio_frame = decoder.decode(frame[1])
                if audio_frame and audio_frame.data:
                    if output == None:
                        output = sound.Output(audio_frame.sample_rate, audio_frame.channels, sound.AFMT_S16_LE)
                    output.play(audio_frame.data)

            while output.isPlaying():
                time.sleep(0.05)

# encoding=utf-8


import codecs

import requests
from bs4 import BeautifulSoup
movie_name_list= []
class qiushi(object):
    def __init__(self):
        self.DOWNLOAD_URL = 'http://www.qiushibaike.com/hot/'
        self.num = 0
        html = self.download_page(self.DOWNLOAD_URL)
        self.parse_html(html)


    def download_page(self,url):
        return requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }).content


    def parse_html(self,html):
        soup = BeautifulSoup(html,"lxml")
        movie_list_soup = soup.find('div', attrs={'id': 'content-left'})

        for movie_li in movie_list_soup.find_all('div', attrs={'class': 'article block untagged mb15'}):
            detail = movie_li.find('div', attrs={'class': 'content'})
            movie_name = detail.find('span').getText()
            # global num
            self.num+=1
            #print self.num,"     ",movie_name
            movie_name_list.append(movie_name)

        return movie_name_list

xiaohuo = qiushi()
xiaohuo.__init__()
print len(movie_name_list)


per = '0'
pit = '5'
spd = '5'
vol = '5'
for aa in movie_name_list:
    tes = aa
    text = tes.replace(u' ', u',')
    text = unicode(text)  # .decode('utf8')
    token = get_token()
    time1 = datetime.datetime.now()
    print token
    getURL = 'http://tsn.baidu.com/text2audio?tex=' + text + '&lan=zh&cuid=123456&ctp=1' + '&per=' + per + '&pit=' + pit + '&spd=' + spd + '&vol=' + vol + '&tok=' + token
    content = urllib2.urlopen(getURL).read()
    file_name=u'temp.mp3'
    f=open(file_name,'wb')
    f.write(content)
    f.close()
    time2 = datetime.datetime.now()
    a  =  time2 - time1
    print  a
    print aa
    playaudio(file_name)
    # time.sleep(3)

#############多进程，下载html，“http://www.qiushibaike.com/hot/page/”+str（page）+“/?s=4932683”
