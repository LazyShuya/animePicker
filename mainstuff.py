#make a different function for gogo anime


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_Options = Options()
chrome_Options.add_argument('load-extension='+'4.14.0_0')

def trans_text(r):
    new_text = r.replace(' ','-')
    tem_tex = new_text.replace('.','\n')
    return tem_tex
class MyAnimeList:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options= chrome_Options)
        self.anime_name = ''
        self.current_link = 'https://myanimelist.net/'
        self.anime_link = ""
        self.driver.get("https://myanimelist.net/")
        self.driver.switch_to_window(self.driver.window_handles[0])
        sleep(5)

    def ret_text(self):
        text = self.anime_link + '/userrecs'
        return text


    def Search(self, keyword):
        link = "https://myanimelist.net/search/all?q="+ keyword
        self.driver.get(link)
        sleep(1)
        self.anime_name = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/a[1]').text
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/a[1]')\
            .click()
        self.anime_link = self.driver.current_url
        print(self.anime_link)
        return self.ret_text()
    
    def redirect(self):     
        main_text = self.anime_name.split('\n')[0]
        main_text = trans_text(main_text)
        self.driver.switch_to_window(self.driver.window_handles[1])
        link2 = f'https://www19.gogoanime.io/{main_text}-episode-1'
        self.driver.get(link2)
        sleep(5)
        return (self.anime_name)
        

    
    