import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MMC_Test(unittest.TestCase):
    def setUp(self):
        Firefox_path = os.getcwd() + '/../../webdriver/'+"geckodriver.exe"
        self.drivcer = webdriver.Firefox(executable_path= Firefox_path)
        self.drivcer.implicitly_wait(15)
        self.drivcer.get('https://mmc-dev.shareitpay.in/#/login')  #打开MMC
    def tearDown(self) -> None:
        time.sleep(2)
        # self.drivcer.quit()
    def test_login_success(self):
        self.drivcer.find_element(By.XPATH,'//input[@type="text"]').send_keys('rensh_sh@ushareit.com')
        self.drivcer.find_element(By.XPATH,'//input[@type="password"]').send_keys('a123456')
        self.drivcer.find_element(By.XPATH,'//button[@type="button"]').click()
        #检查是否登录成功
        time.sleep(5)
        self.drivcer.find_element(By.XPATH,'//div[@class="user-name-div"]').click()
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH,'//li[@class="el-dropdown-menu__item is-disabled"]'),'rensh_sh@ushareit.com')
        a = self.drivcer.find_element(By.XPATH,'//li[@class="el-dropdown-menu__item is-disabled"]').text
        return a

if __name__ == '__main__':
    n = unittest.main()
    n.addd