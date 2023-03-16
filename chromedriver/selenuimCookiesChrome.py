import time
import pickle
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from auth_data import user_name, user_password, name, password

url = "https://instagram.com/"

user_agent = UserAgent()
options = webdriver.ChromeOptions()

options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
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
