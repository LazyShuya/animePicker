import requests
from bs4 import BeautifulSoup

def get_recs(url):
    
    plain_html_text = requests.get(url)
    soup = BeautifulSoup(plain_html_text.content, "html.parser")
    soup.prettify()
    content = soup.find_all('strong')
    record = [i.string for i in content if not (i.string).isdigit() ]
    return record
