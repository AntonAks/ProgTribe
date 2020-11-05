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
            if "https://" in a.get('href') and len(str(a.getText())) > 2:
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip())

    return post_names, post_urls


def get_kor_news() -> tuple:
    site = "https://korrespondent.net/business/web/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    items = soup.find_all(class_='article article_rubric_top')

    post_names = []
    post_urls = []

    for i in items:
        a_tags = i.find_all('a')
        for a in a_tags:
            if len(str(a.getText())) > 2 and "https://" in a.get('href') :
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip().replace("Сюжет", ""))


    return post_names, post_urls


def get_tproger_news() -> tuple:
    site = "https://tproger.ru/top/month/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    items = soup.find_all(class_='article-link')
    text = soup.find_all(class_='entry-title')

    post_names = []
    post_urls = []

    for i in range(0, len(items)):
        post_names.append(text[i].getText())
        post_urls.append(items[i].get('href'))

    return post_names, post_urls


def get_ain_news() -> tuple:

    site = "https://ain.ua/post-list/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    items = soup.find_all(class_='post-link with-labels')

    post_names = []
    post_urls = []

    for i in items:
        texts = i.find_all(text=True)
        for text in texts:
            if len(text) > 3:
                post_names.append(str(text).strip())

        if len(str(i.getText())) > 2 and "https://" in i.get('href'):
            post_urls.append(i.get('href'))

    return post_names, post_urls


if __name__ == '__main__':
    pass
