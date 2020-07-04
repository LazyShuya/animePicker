from recs_database import add_recs, update, random_function
import scraper
from watching import new_watching, update_episode 
from mainstuff import MyAnimeList as MAL

#need to complete this function
#make a gogoanime navigator
def continue_leftoff():
    return

page = MAL()
search = page.Search(random_function())
anime_list = scraper.get_recs(search[0])
first_episode = page.redirect()
add_recs(first_episode[0], search[1], anime_list)
new_watching(first_episode[1],first_episode[2])
update()
#  be able to remove . from text
#make a timer every 25 min check gogo anime handle and get the ep no
#make a sparate script for scraping
#use functions instead of classes
