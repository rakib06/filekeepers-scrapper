
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
# from selenium.webdriver.chrome.options import Options


def local():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def docker_remote():
    time.sleep(5)
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['chromeOptions'] = {
        "args": ["--no-sandbox"],
    }
    driver = webdriver.Remote('http://selenium:4444/wd/hub',
                              desired_capabilities=desired_capabilities
                              )
    return driver
