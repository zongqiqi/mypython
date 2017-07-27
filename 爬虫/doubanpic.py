# encoding=utf-8

import os
import requests
import urllib
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://book.douban.com/top250?icn=index-book250-all'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

i = 0



def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    book_list_soup = soup.find('div', attrs={'class': 'indent'})
    book_name_list = []
    bookadrss = []
    for book_li in book_list_soup.find_all('table',attrs={'width':'100%'}):
        detail = book_li.find('div',attrs={'class':'pl2'})
        book_name = detail.find('a').getText("",strip=True)
        book_name_list.append(book_name)
        adress = detail.find('a').get('href')

        bookadrss.append(adress)
        global i
        i +=1
    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return book_name_list,bookadrss,next_page['href']
    return book_name_list,bookadrss, None

def picc(url):
    url1 = download_page(url)
    soup = BeautifulSoup(url1, "lxml")
    detail = soup.find('div', attrs={'id': 'mainpic'})
    adress = detail.a['href']
    return  adress


y = 1
def save_pic(url) :
    save_path = u'图片'
    global y
    name = save_path + "/" + str(y) + ".jpg"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    conn = urllib.urlopen(url)
    print str(y),'saved'
    f = open(name,'wb')
    f.write(conn.read())
    y += 1
    f.close()


def main():
    url = DOWNLOAD_URL
    while url:
        html = download_page(url)
        books,adress, url = parse_html(html)
        for book in adress:
            try:
                picadress = picc(book)
                save_pic(picadress)
            except:
                pass
        print 'work is done,see you next time'


if __name__ == '__main__':
    main()