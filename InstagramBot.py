from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login']")
        #login_button.click()
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for i in range(1,4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if '/p/' in href]
        print(pic_hrefs)
        for pic_href in pic_hrefs:
            print(pic_href)
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            driver.find_element_by_class_name('_8-yf5').click()
            time.sleep(10)
            print("hello")








        # "//a[@href'accounts/login']"
        # "//input[@name='username']"
        # "//imput[@name='password']"

bot = InstagramBot('morgantic.t','WandaRat11')


bot.login()
hashtags = ["sanfransisco", "fashionblogger", "aesthetic"]
for hashtag in hashtags:
    bot.like_photo(hashtag)
bot.close_browser()



