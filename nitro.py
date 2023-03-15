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
        self.login_saved = True
        
        # typing info
        self.time_between_key_presses = 250 # in milliseconds
        self.words = []
        
        # session info
        self.session = False
        self.driver = None

        # racing info
        self.currently_racing = False
        self.auto_race = False

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
        
    # write user info to file
    def write_users(self):
        # save to file
        userinfo = open(self.userinfo, "w")
        for user in self.users.keys():
            userinfo.write(f"{user},{self.users[user]}\n")

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
        
        # userfile = open(userinfo, "w+")
        # prev = userfile.read()
        # new_info = f"{username},{password}\n"
        # userfile.write(new_info + prev)
        # userfile.close()
        return username, password
    
    def sign_in(self, username, password):
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div.g.g--f.well.well--b.well--xxl > div.g-b.g-b--7of12 > div > div > div > div > div:nth-child(2) > a").click()
        except:
            pass

        try:
            # locate input fields
            u = self.driver.find_element(By.ID, "username")
            p = self.driver.find_element(By.ID, "password")
            
            # clear input fields
            u.clear()
            p.clear()

            u.send_keys(username)
            p.send_keys(password)
        
            btns = self.driver.find_elements(By.CLASS_NAME, "btn--fw")
            for b in btns:
                if b.text == "Log In": 
                    b.click()
        except:
            print("login failed")
        
    def race_now(self):
        time.sleep(2.5)
        first_time = True
        
        self.currently_racing = True

        # while loop for auto racing
        while first_time or self.auto_race:
            first_time = False
            try:
                # self.driver.find_element(By.XPATH, "//*[text()='Race Now']").click()
                btns = self.driver.find_elements(By.CLASS_NAME, "well--s")
                for b in btns:
                    if b.text == "Race Now" or b.text == "Race Again": 
                        b.click()
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.RETURN).perform()
            except Exception as e:
                if type(e) == NoSuchElementException:
                    print("racing failed")
                    # self.sign_up()
                    self.driver.find_element(By.XPATH, "//*[text()='Race Now']").click()
        
            while True:
                try:
                    self.driver.find_element(By.CLASS_NAME, "dash-letter")
                    time.sleep(4)
                    break
                except:
                    pass

            self.locate_words()
            self.bot_thread(self.type_words)
            time.sleep(30)
        self.currently_racing = False

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

    def save_login(self, username, password):
        self.users[username] = password

    def toggle_save_login(self):
        self.login_saved = not self.login_saved

    def bot_thread(self, function, *args):
        thread = threading.Thread(target=function, args=args)
        thread.start()
    
    def toggle_auto(self):
        self.auto_race = not self.auto_race

    # def automatic_racing(self):
    #     while self.auto_race:
    #         print("an iteration of automatic racing has been started.")
    #         thread = threading.Thread(target=self.bot_thread, args=(self.race_now,))
    #         thread.start()
    #         thread.join()
            
if __name__ == "__main__":
    bot = Nitro_Bot()
    bot.sign_in("Troy75318", bot.users["Troy75318"])
    print(bot.generate_new_login_info("test"))
    keyboard.wait('esc')
