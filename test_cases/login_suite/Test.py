import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


Firefox_path = os.getcwd() + '/../../webdriver/'+"geckodriver.exe"
drivcer = webdriver.Firefox(executable_path= Firefox_path)
drivcer.implicitly_wait(15)
drivcer.get('https://mmc-dev.shareitpay.in/#/login')  #打开MMC
drivcer.find_element(By.XPATH,'//input[@type="text"]').send_keys('rensh_sh@ushareit.com')
drivcer.find_element(By.XPATH,'//input[@type="password"]').send_keys('a123456')
drivcer.find_element(By.XPATH,'//button[@type="button"]').click()
#检查是否登录成功
drivcer.find_element(By.XPATH,'//div[@class="user-name-div"]').click()
# assertTrue(EC.text_to_be_present_in_element(By.XPATH,'//li[@class="el-dropdown-menu__item is-disabled"]'),'rensh_sh@ushareit.com')
a = drivcer.find_element(By.XPATH,'//li[@class="el-dropdown-menu__item is-disabled"]').text
print(a)