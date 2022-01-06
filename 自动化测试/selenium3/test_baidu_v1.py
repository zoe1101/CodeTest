import unittest
from time import sleep
from selenium import webdriver


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_search_key_selenium(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.assertEqual(self.driver.title, 'selenium_百度搜索')

    def test_search_key_unttest(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        sleep(2)
        self.assertEqual(self.driver.title, "unittest_百度搜索")

if __name__ == '__main__':
    unittest.main()
