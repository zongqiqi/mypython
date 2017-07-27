# encoding=utf-8

import codecs
import url_parse
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://book.douban.com/top250?icn=index-book250-all'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

i = 0
book_name_list = []
bookadrss = []
def my_pic(url):
    url1 = download_page(url)
    soup = BeautifulSoup(url1,"lxml")
    detail = soup.find('div',attrs={'id':'mainpic'})
    adress = detail.find('a').get('href')
    return adress

def parse_html(html):
    soup = BeautifulSoup(html,"lxml")
    book_list_soup = soup.find('div', attrs={'class': 'indent'})



    for book_li in book_list_soup.find_all('table',attrs={'width':'100%'}):
        detail = book_li.find('div',attrs={'class':'pl2'})
        book_name = detail.find('a').getText("",strip=True)
        book_name_list.append(book_name)
        adress = detail.find('a').get('href')
        bookadrss.append(adress)
        #pic = url_parse.m_pic(adress,'div','id','mainpic')
        global i
        i +=1

        print i,"    ", book_name,"    ",adress#,'图片',pic

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return book_name_list,bookadrss,next_page['href']
    return book_name_list,bookadrss, None


def main():
    url = DOWNLOAD_URL

    with codecs.open('books', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            books,adress, url = parse_html(html)
            fp.write(u'{books}\n'.format(books='\n'.join(books)))
    #for book in book_name_list:
        #print  book
    #for adress in bookadrss:
       # print adress
if __name__ == '__main__':
    main()