from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from fake_useragent import UserAgent


url_3 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"


user_agent = UserAgent()
options = webdriver.FirefoxOptions()
# options.set_preference("general.useragent.override", "Hello Friend")
options.set_preference("general.useragent.override", user_agent.random)


driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)


try:
    driver.get(url=url_3)
    time.sleep(2)
    driver.get_screenshot_as_file("1.png")
    driver.refresh()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
