
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def local():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def docker_remote():
    driver = webdriver.Remote('http://selenium:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME,
                              )
    return driver
