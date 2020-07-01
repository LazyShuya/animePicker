import requests
from bs4 import BeautifulSoup as bs

def get_webpage(url):
    webpage = requests.get(url).text
    soup = bs(webpage, 'html.parser')
    return soup


def get_recs(url):
    record = []
    soup = get_webpage(url)
    content = soup.find_all("strong")
    record = [i.string for i in content if not (i.string).isdigit()]
    return record