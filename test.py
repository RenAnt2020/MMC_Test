from selenium.webdriver.common.by import By
from common import set_driver,config,login
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
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
        self.driver.find_element(By.XPATH, '//div/ul/div/li/ul/li[2]').click()

    def test_query3(self):
        self.driver.find_element(By.XPATH, '//div/ul/div/li/ul/li[3]').click()



# if __name__ == '__main__':
    # test = unittest.TestSuite()
    # test.addTest(Orderquery_test('test_query1'))
    # unittest.main(defaultTest='test')


current_path = os.path.dirname(__file__)
report_path = os.path.join(current_path,'report')
cases_path = os.path.join(current_path,'test_cases')
html_path = os.path.join(report_path,"report_%s.html"%time.strftime('%Y_%m_%d_%H_%M_%S'))
# discover = unittest.defaultTestLoader.discover(start_dir=cases_path,pattern='*_case.py',
#                                                top_level_dir=cases_path)

main_suite = unittest.TestSuite()
main_suite.addTest(Orderquery_test('test_query1'))
file = open(html_path,'wb')
html_runner = HTMLTestRunner(stream=file,title='MMC自动化测试项目',description='由华仔搭建，逐渐完善中')
html_runner.run(main_suite)
