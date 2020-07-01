from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_Options = Options()
chrome_Options.add_argument('load-extension='+'4.14.0_0')

class AnimeBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options= chrome_Options)
        sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[1])
        # self.driver.close()
        # # self.driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
        # # self.driver.switch_to_window(self.driver.window_handles[1])
        # # self.driver.get("https://www.edureka.co/community/52772/close-active-current-without-closing-browser-selenium-python")
        # self.driver.switch_to_window(self.driver.window_handles[0])
        sleep(2)
        self.driver.get("https://www19.gogoanime.io/naruto-episode-1")
        self.driver.switch_to_window(self.driver.window_handles[0])
        sleep(2)
        self.driver.find_element_by_tag_name("html").send_keys(Keys.CONTROL + 'T')
        # self.iframeElement = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section[1]/div[1]/div[2]/div[3]/div/div/div/iframe')
        # self.driver.switch_to.frame(self.iframeElement)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/section/section[1]/div[1]/div[2]/div[3]/div/div/div').click()
        
        sleep(50)
        

AnimeBot()