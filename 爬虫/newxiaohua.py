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
        aaa = self.parse_html(html)


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

