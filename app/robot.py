from time import sleep

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

# driver = webdriver.Remote(command_executor='http://selenium:4444/wd/hub',
#                           desired_capabilities=DesiredCapabilities.CHROME)

print("Test Execution Started")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get('https://python.org')
driver.save_screenshot('screenshot.png')
