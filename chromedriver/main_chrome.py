# from selenium import webdriver
from seleniumwire import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from proxy_auth_data import login, password


url_1 = "https://www.instagram.com"
url_2 = "https://stackoverflow.com"
url_3 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
url_4 = "https://2ip.ru"


user_agent_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

user_agent = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--proxy-server=94.131.130.142:8085")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    seleniumwire_options=proxy_options
)


try:
    driver.get(url=url_2)
    time.sleep(2)
    driver.get_screenshot_as_file("1.png")
    driver.refresh()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
