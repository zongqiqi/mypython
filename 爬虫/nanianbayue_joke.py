# encoding=utf-8


import codecs

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://yidao620c.github.io/2020/03/07/joke.html'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_list_soup = soup.find('div', attrs={'class': 'post-content'})

    movie_name_list = []
    i = 0
    for movie_li in movie_list_soup.find_all('p'):
        i+=1
        detail = movie_li.getText()
        detail = detail.replace("\n","")
        print i,"                ",detail
        movie_name_list.append(detail)


    return movie_name_list, None


def main():
    url = DOWNLOAD_URL
    try:
        html = download_page(url)
        movies, url = parse_html(html)
    except:
        print "this one crawl is done!  NEED HELP`"


if __name__ == '__main__':
    main()
