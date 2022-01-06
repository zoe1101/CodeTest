'''
每一条测试用例都要启动和关闭一次浏览器，这是非常耗时的，那么如何减少浏览器的启动和关闭次数呢？
利用前面学过的 setUpClass/tearDownClass 可以解决这个问题。

虽然我们将 driver 驱动定义为 cls.driver，但是在每个测试用例中使用时依然为self.driver。
当整个测试类中的所有测试用例都运行完成后，会调用 cls.driver.quit()关闭浏览器。
当一个测试类中有多条测试用例时，这种方式将大大缩短测试用例的执行时间。
'''

import unittest
from time import sleep
from selenium import webdriver

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

    def test_search_key_selenium(self):
        search_key = 'selenium'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    def test_search_key_unttest(self):
        search_key = 'unittest'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')


if __name__ == '__main__':
    unittest.main()
