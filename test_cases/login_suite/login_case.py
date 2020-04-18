import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver,login,config

class Login_Test(unittest.TestCase):
    def setUp(self):
        self.driver=set_driver.set_driver()
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_login_success(self):
        login.login(self.driver,config.username(),config.password())        #检查是否登录成功
        self.assertTrue(EC.visibility_of(self.driver.find_element(By.XPATH,'//div[@class="user-name-div"]')))

if __name__ == '__main__':
    unittest.main()