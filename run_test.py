import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from test_cases.Order_query import OrderSearch_case

current_path = os.path.dirname(__file__)
report_path = os.path.join(current_path,'report')
cases_path = os.path.join(current_path,'test_cases')
html_path = os.path.join(report_path,"report_%s.html"%time.strftime('%Y_%m_%d_%H_%M_%S'))
discover = unittest.defaultTestLoader.discover(start_dir=cases_path,pattern='*_case.py',
                                               top_level_dir=cases_path)

main_suite = unittest.TestSuite
main_suite.addTest(OrderSearch_case.Orderquery_test('test_query_success'))
file = open(html_path,'wb')
html_runner = HTMLTestRunner(stream=file,title='MMC自动化测试项目',description='由华仔搭建，逐渐完善中')
html_runner.run(main_suite)