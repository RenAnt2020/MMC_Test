import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver,config,login

class Orderquery_test(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver.set_driver()
        login.login(self.driver, config.username(), config.password()) #登录
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()
    def test_query1(self):
        self.driver.find_element(By.XPATH,'//div/ul/div/li/ul/li[1]').click()

    def test_query2(self):
        self.driver.find_element(By.XPATH, '//div/ul/div/li/ul/li[1]').click()

    def test_query3(self):
        self.driver.find_element(By.XPATH, '//div/ul/div/li/ul/li[1]').click()



if __name__ == '__main__':
    test = unittest.TestSuite()
    test.addTest(Orderquery_test('test_query1'))
    unittest.main(defaultTest='test')


