import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from background_task import background


def get_dou_news() -> tuple:

    site = "https://dou.ua/lenta/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    items = soup.find_all(class_='title')

    post_names = []
    post_urls = []

    for i in items:
        a_tags = i.find_all('a')
        for a in a_tags:
            if "https://" in a.get('href'):
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip())

    return post_names, post_urls


def get_itc_news() -> tuple:

    site = "https://itc.ua/news/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    items = soup.find_all(class_='entry-title text-uppercase')

    post_names = []
    post_urls = []

    for i in items:
        a_tags = i.find_all('a')
        for a in a_tags:
            if "https://" in a.get('href'):
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip())

    return post_names, post_urls


def get_liga_news() -> tuple:
    site = "https://tech.liga.net/technology"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    items = soup.find_all(class_='news')

    post_names = []
    post_urls = []

    for i in items:
        a_tags = i.find_all('a')
        for a in a_tags:
            if "https://" in a.get('href'):
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip())

    return post_names, post_urls


if __name__ == '__main__':
    pass
