import requests
from bs4 import BeautifulSoup
import os

def toi_spider(max_p, section):
    page = 1
    if section == '':
        path = 'Homepage'
    else:
        path = section
    if not os.path.exists(path):
        os.makedirs(path)
    f = path + '/' + path + ' news.txt'
    file = open(f, 'w', encoding="iso-8859-1")
    while page <= max_p:
        s_url = 'https://timesofindia.indiatimes.com/' + section
        if page == 1:
            url = s_url
        else:
            url = s_url + '/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a'):
            href =str(link.get('href'))
            if href[:41]=="https://timesofindia.indiatimes.com/india":
                news_data(href, file)
        page += 1

def news_data(news_url, file):
    source_code = requests.get(news_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    titl = 'none'
    for title in soup.findAll('h1', {'class': '_23498'}):
        titl = title.string
    for date in soup.findAll('div', {'class': '_3Mkg- byline'}):
        d_t = date.get_text()
    for text in soup.findAll('div', {'class': 'ga-headlines'}):
        txt = text.get_text()
    if titl != 'none':
        file.write('Title:' + '\n')
        file.write(titl + '\n\n')
        file.write('Link:' + '\n')
        file.write(news_url + '\n\n')
        file.write('Date & Time:' + '\n')
        file.write(d_t + '\n\n')
        file.write('Text:' + '\n')
        file.write(txt + '\n\n\n')


toi_spider(12, 'india')
toi_spider(1, 'world')
toi_spider(1, 'business')
toi_spider(1, '')

