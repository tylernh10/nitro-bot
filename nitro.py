from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import time
import random
import names
import threading
from string import ascii_letters, digits

class Nitro_Bot():
    def __init__(self):
        self.nitro_url = "https://nitrotype.com"
        
        # credentials info
        self.userinfo = "userinfo.txt"
        self.users = dict()
        
        # typing info
        self.time_between_key_presses = 500 # in milliseconds
        self.words = []
        
        # session info
        self.session = False
        self.driver = None

        # open user info file, create if does not exist
        userinfofile = open(self.userinfo, "r+")
        for line in userinfofile.readlines():
            info = line.split(',')
            u = info[0].strip()
            p = info[1].strip()
            self.users[u] = p
        # self.username = "Troy75318"
        # self.password = self.users[self.username]

    def initialize_driver(self):
        # no session until initialization happens
        self.session = False
        self.driver = None
        
        # initialize webdriver
        service = Service('./chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.nitro_url)
        time.sleep(3)
        self.session = True
        

    def destroy(self):
        self.driver.close()

    def write_char(self, char, actions):
        # keyboard.write(char)
        actions.send_keys(char).perform()
        time.sleep(self.time_between_key_presses / 1000)

    # called if the signin info is invalid
    def sign_up(self, username, password):
        self.driver.find_element(By.XPATH, "//*[text()='Sign Up Now!']").click()
        # self.username, self.password = self.generate_new_login_info(self.userinfo)

        time.sleep(12)
        self.locate_words()
        self.type_words()
        time.sleep(12)
        
        # get signin elements and populate
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[text()='Sign up with Username']").click()
        time.sleep(10)

    def generate_new_login_info(self, userinfo):
        # generates a new username and saves it to the file specified
        username = names.get_first_name()
        for i in range(5):
            username += random.choice(digits)
        password = ""
        for i in range(32):
            choice = random.randint(0, 1)
            if choice:
                password += random.choice(ascii_letters)
            else:
                password += random.choice(digits)
        
        userfile = open(userinfo, "w+")
        prev = userfile.read()
        new_info = f"{username},{password}\n"
        userfile.write(new_info + prev)
        userfile.close()
        return username, password
    
    def sign_in(self, username, password):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div.g.g--f.well.well--b.well--xxl > div.g-b.g-b--7of12 > div > div > div > div > div:nth-child(2) > a").click()
        except:
            pass

        try:
            self.driver.find_element(By.ID, "username").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
        
            btns = self.driver.find_elements(By.CLASS_NAME, "btn--fw")
            for b in btns:
                if b.text == "Log In": 
                    b.click()
        except:
            print("login failed")
        
    def race_now(self):
        time.sleep(3.70)
        try:
            self.driver.find_element(By.XPATH, "//*[text()='Race Now']").click()
        except Exception as e:
            if type(e) == NoSuchElementException:
                self.sign_up()
                self.driver.find_element(By.XPATH, "//*[text()='Race Now']").click()
        
        time.sleep(12)
        self.locate_words()
        self.bot_thread(self.type_words)

    def locate_words(self):
        self.words = self.driver.find_elements(By.CLASS_NAME, "dash-word")

    def type_words(self):
        actions = ActionChains(self.driver)
        for word in self.words:
            text = word.text
            for char in text:
                self.write_char(char, actions)

    # returns boolean based on fact if session has been started yet or not
    def valid_session(self):
        return self.session
    
    def update_speed(self, speed):
        self.time_between_key_presses = speed

    def bot_thread(self, function, *args):
        thread = threading.Thread(target=function, args=args)
        thread.start()

if __name__ == "__main__":
    bot = Nitro_Bot()
    bot.sign_in()
    keyboard.wait('esc')
    bot.destroy()
