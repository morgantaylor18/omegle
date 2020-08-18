from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




response_dict2 = {"hey": "yes ;) my snap is morgan_t18",
                 "bet": "bet my snap is morgan_t18 :)",
                 "m": "age? my snap is morgan_t18 :)",
                 "no": ":(",
                 "yes ya yeah maybe snap": "add me snap is morgan_t18 :)"}
DEFAULT_RESPONSE = 'hey'

class OmegleBot:

    def __init__(self, message):
        self.message = message

        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def logon(self):
        driver = self.driver
        driver.get("https://www.omegle.com/")  # go to Omegle
        time.sleep(2)

        driver.find_element_by_id("textbtn").click()  # go to text chat
        time.sleep(3)

        # chat_elem = driver.find_element_by_class_name("inconversation")
        # chat_elem.send_keys(self.message)
        # chat_elem.send_keys(Keys.RETURN)
        # time.sleep(2)

    def new_chat(self):
        driver = self.driver
        # if button says new press it to start a new chat
        if self.check_new_button():
            driver.find_element_by_class_name('disconnectbtn').click()

    def start_chat(self):
        driver = self.driver
        try:
            chat_elem = driver.find_element_by_class_name("inconversation")
            chat_elem.send_keys(self.message)
            chat_elem.send_keys(Keys.RETURN)
        except:
            pass
        chat_elem = None

    def stop_chat(self):
        driver = self.driver
        # stranger has not ended the chat, end it
        if self.check_stop_button():
            driver.find_element_by_class_name('disconnectbtn').click()
            driver.find_element_by_class_name('disconnectbtn').click()
            time.sleep(1)
            return True
        else:  # otherwise it already ended
            return False
        # returns true if chat was ended and false otherwise

    def check_for_response(self):
        driver = self.driver

        try:
            class_name = driver.find_element_by_class_name("strangermsg")
            return True, class_name.text[10:].lower()
        except:
            return False, "no message"

        # if driver.find_element_by_class_name("strangermsg"):
        #     class_name = driver.find_element_by_class_name("strangermsg")
        #     print(class_name.text[10:])  # for testing
        #     return True, class_name.text[10:].lower()  # reply, respond to it
        # else:
        #     return False, "no message"  # no reply

    def reply(self, reply_with_this):
        driver = self.driver
        if self.check_stop_button:
            try:
                chat_elem = driver.find_element_by_class_name("inconversation")
                chat_elem.send_keys(reply_with_this)
                chat_elem.send_keys(Keys.RETURN)
            except:
                pass
        else:
            pass

    def search_responses(self, response):
        for key in response_dict:
            if response in key:
                return response_dict[key]
        return DEFAULT_RESPONSE

    def check_stop_button(self):
        driver = self.driver

        stuff = driver.find_element_by_class_name('disconnectbtn')

        if stuff.text == "Stop\nEsc":
            return True
        else:
            return False

    def check_new_button(self):
        driver = self.driver

        stuff = driver.find_element_by_class_name('disconnectbtn')

        if stuff.text == "New\nEsc":
            return True
        else:
            return False

morgan = "morgan_t18"
shae = "scawley97"

message = "I'm F22 selling nudes and videos my snap is " + morgan + " ;) "

# while
# if j % 2 == 0:
#     bot = OmegleBot("I'm F22 selling nudes and videos my snap is " + morgan + " ;) ")
bot = OmegleBot(message)

bot.logon()  # starts initial chat
time.sleep(1)
while True:
    i = 0
    while i < 1:
        bot.start_chat()  # sends message
        i += 1
    time.sleep(5)   # response time
    responded, message = bot.check_for_response()
    if responded:
        reply_with = bot.search_responses(message)
        bot.reply(reply_with)
        time.sleep(1)
    bot.stop_chat()  # stops chat if stranger didn't
    time.sleep(1)
    bot.new_chat()  # starts new chat
    time.sleep(4)
