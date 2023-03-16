from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url_1 = "https://www.instagram.com"
url_2 = "https://stackoverflow.com"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.get(url=url_1)
    time.sleep(2)
    driver.get_screenshot_as_file("1.png")
    driver.get(url=url_2)
    time.sleep(2)
    driver.get_screenshot_as_file("2.png")
    driver.refresh()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
