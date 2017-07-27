import requests
from bs4 import BeautifulSoup
a='div'
b='id'
c='mainpic'
def m_pic(url,a,b,c):
    def download_page(url):
        return requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }).content

    url1 = download_page(url)
    soup = BeautifulSoup(url1,"lxml")
    detail = soup.find(str(a),attrs={b:c})
    adress = detail.find('a').get('href')
    return adress
