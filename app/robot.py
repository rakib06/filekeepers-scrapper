from time import sleep

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from utils.config import *

sleep(5)
print("Test Execution Started")


driver = webdriver.Remote('http://selenium:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.CHROME,
                          )


driver.get(URL)
driver.save_screenshot('screenshot.png')
