from recs_database import add_recs, update, random_function
import scraper
from mainstuff import MyAnimeList as MAL

page = MAL()
search = page.Search(random_function())
anime_list = scraper.get_recs(search[0])
add_recs(page.redirect(), search[1], anime_list)
update()
#  be able to remove . from text
#make a timer every 25 min check gogo anime handle and get the ep no
#make a sparate script for scraping
#use functions instead of classes