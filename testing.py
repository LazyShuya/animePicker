from recs_database import add_recs
import scraper
from mainstuff import MyAnimeList as MAL

page = MAL()
anime_list = scraper.get_recs(page.Search('asobi asobase'))
add_recs(page.redirect(), anime_list)
update()
#  be able to remove . from text
#make a timer every 25 min check gogo anime handle and get the ep no
#make a sparate script for scraping
#use functions instead of classes