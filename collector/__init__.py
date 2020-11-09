import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import json
from background_task import background


def get_currency() -> list or None:

    resp = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")

    if resp.status_code == 200:
        return json.loads(resp.text)


def get_dou_news_it() -> tuple:

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


def get_itc_news_it() -> tuple:

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


def get_liga_news_it() -> tuple:
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


def get_ain_news_it() -> tuple:

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


def get_liga_news_fin() -> tuple:
    site = "https://finance.liga.net/news"
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
            if "https://" in a.get('href') and len(str(a.getText())) > 2 and 'ЛІГА.' not in a.getText():
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip())

    return post_names, post_urls


def get_investing_fin() -> tuple:
    site = "https://ru.investing.com/news/latest-news"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    leftColumn = soup.find(id='leftColumn')

    items = leftColumn.find_all(class_='textDiv')

    post_names = []
    post_urls = []

    for i in items:
        title_name = i.find_all(class_='title')[0].get('title')
        url_name = i.find_all(class_='title')[0].get('href')
        if len(title_name) > 3:
            post_names.append(title_name)
            post_urls.append('https://ru.investing.com'+url_name)

    return post_names, post_urls


def get_kor_news_world() -> tuple:
    site = "https://korrespondent.net/world/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    unit_rubric = soup.find(class_='unit-rubric')

    items = unit_rubric.find_all(class_='article__title')

    post_names = []
    post_urls = []

    for i in items:
        a_tags = i.find_all('a')
        for a in a_tags:
            if len(str(a.getText())) > 2 and "https://" in a.get('href'):
                post_urls.append(a.get('href'))
                post_names.append(str(a.getText()).strip().replace("Сюжет", ""))

    return post_names, post_urls


def get_euro_news_world() -> tuple:
    site = "https://ru.euronews.com/programs/world"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, "html.parser")

    listing_articles_block = soup.find(class_='o-block-listing__articles')

    articles = listing_articles_block.find_all(class_='m-object__title__link')

    post_names = []
    post_urls = []

    for i in articles:
        post_names.append(i.getText().strip())
        post_urls.append('https://ru.euronews.com' + i.get('href'))

    return post_names, post_urls


