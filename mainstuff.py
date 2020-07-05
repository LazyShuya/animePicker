#make a different function for gogo anime


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_Options = Options()
chrome_Options.add_argument('load-extension='+'4.14.0_0')

class MyAnimeList:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options= chrome_Options)
        self.anime_name = 'Yu☆Gi☆Oh! '
        self.current_link = 'https://myanimelist.net/'
        self.anime_link = ""
        self.driver.get("https://myanimelist.net/")
        self.driver.switch_to_window(self.driver.window_handles[0])
        sleep(5)

    def ret_text(self):
        text = self.anime_link + '/userrecs'
        return text


    def Search(self, keyword):
        self.driver.switch_to_window(self.driver.window_handles[0])
        link = "https://myanimelist.net/search/all?q="+ keyword
        self.driver.get(link)
        sleep(1)
        self.anime_name = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/a[1]').text
        
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div/article[1]/div[1]/div[2]/a[1]')\
            .click()
        Total_episodes = self.driver.find_element_by_xpath("//div[contains(text(), 'Episodes:')]").text
        episodes = (''.join(filter(str.isdigit, Total_episodes)))
        self.anime_link = self.driver.current_url
        print(self.anime_link)
        print(episodes)
        return [self.ret_text(), int(episodes)]
    
    def redirect(self):     
        main_text = self.anime_name
        link = 'https://www19.gogoanime.io/'
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get(link)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/header/section/div[4]/div[1]/form/div[1]/input[1]')\
            .send_keys(main_text)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/header/section/div[4]/div[1]/form/div[1]/input[2]').click()
        
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section[1]/div/div[2]/ul/li[1]/div/a/img').click()
        to_edit = self.driver.current_url
        ep_link = to_edit.replace('/category/', '/')
        self.driver.get(ep_link + '-episode-1')
        return [self.anime_name, ep_link + '-episode-', '1']


    def continue_where_left(self, link_ref):
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get(link_ref)

    def current_episode(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        episode = self.driver.find_element_by_class_name('default_ep').get_attribute('value')
        return int(episode)


    def exit_program(self):
        ep = self.current_episode()
        self.driver.quit()
        return ep

    def simple_exit(self):
        self.driver.quit()