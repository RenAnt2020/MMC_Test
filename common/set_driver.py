import os
from selenium import webdriver
from common import config
def set_driver():
    Firefox_path = os.path.dirname(__file__) + '/../webdriver/' + "geckodriver.exe"
    driver = webdriver.Firefox(executable_path=Firefox_path)
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get(config.url())  # 打开MMC
    return driver

if __name__ == '__main__':
    set_driver()