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

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

# try:
#     driver.get(url=url)
#     time.sleep(5)
#
#     username_input = driver.find_element(By.NAME, user_name)
#     username_input.clear()
#     username_input.send_keys(name)
#     time.sleep(2)
#
#     password_input = driver.find_element(By.NAME, user_password)
#     password_input.clear()
#     password_input.send_keys(password)
#     time.sleep(2)
#
#     password_input.send_keys(Keys.ENTER)
#     time.sleep(5)
#
#     pickle.dump(driver.get_cookies(), open(f"{name}_cookies", "wb"))
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

try:
    driver.get(url=url)
    time.sleep(5)

    for cookie in pickle.load(open(f"{name}_cookies", "rb")):
        print(cookie)
        driver.add_cookie(cookie)

    time.sleep(5)

    driver.refresh()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
