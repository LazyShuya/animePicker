import requests
from bs4 import BeautifulSoup as bs

def get_webpage(url):
    webpage = requests.get(url).text
    soup = bs(webpage, 'html.parser')
    return soup


def get_recs(url):
    record = []
    soup = get_webpage(url)
    content = soup.find_all(style="margin-bottom: 2px;")
    for stuff in content:
        record.append(stuff.find('strong').get_text())
    return record

