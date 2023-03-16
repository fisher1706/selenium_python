import time
import pickle

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

from auth_data import name, password, user_name, user_password

url = "https://instagram.com/"

user_agent = UserAgent()
options = webdriver.FirefoxOptions()

options.set_preference("general.useragent.override", user_agent.random)
options.set_preference("dom.webdriver.enabled", False)
options.add_argument("--headless")

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

try:
    driver.get(url=url)
    time.sleep(5)

    print("Passing authentication...")
    username_input = driver.find_element(By.NAME, user_name)
    username_input.clear()
    username_input.send_keys(name)
    time.sleep(2)

    password_input = driver.find_element(By.NAME, user_password)
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(2)

    password_input.send_keys(Keys.ENTER)
    print("Finish authentication...")

    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

