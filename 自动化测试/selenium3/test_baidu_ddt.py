'''
DDT（ Data-Driven Tests）是针对 unittest 单元测试框架设计的扩展库。允许使用不同的测试数据来运行一个测试用例，并将其展示为多个测试用例。
用 DDT 需要注意以下几点。
首先，测试类需要通过@ddt 装饰器进行装饰。
其次， DDT 提供了不同形式的参数化。
DDT 还支持 yaml 格式的数据文件
'''

import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, data, file_data, unpack

class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    # 参数化使用方式一
    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    @unpack
    def test_search1(self, case, search_key):
        print("第一组测试用例： ", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化使用方式二
    @data(("case1", "selenium"), ("case2", "ddt"), ("case3", "python"))
    @unpack
    def test_search2(self, case, search_key):
        print("第二组测试用例： ", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化使用方式三
    @data({"search_key": "selenium"}, {"search_key": "ddt"}, {"search_key":"python"})
    @unpack
    def test_search3(self, search_key):
        print("第三组测试用例： ", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")
    # 参数化读取 JSON 文件
    @file_data('ddt_data_file.json')
    def test_search4(self, search_key):
        print("第四组测试用例： ", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化读取 yaml 文件
    @file_data('ddt_data_file.yaml')
    def test_search5(self, case):
        search_key = case[0]["search_key"]
        print("第五组测试用例： ", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")
if __name__ == '__main__':
    unittest.main(verbosity=2) #verbosity：指定日志的级别，默认为 1。 如果想得到更详细的日志， 则可以将参数修改为 2。
