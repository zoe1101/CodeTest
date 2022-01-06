'''
封装方法。将百度首页的访问和搜索过程封装成一个 baidu_search()方法，并定义 search_key
参数为搜索关键字，根据接收的关键字执行不同内容的搜索
'''
'''
测试用例的断言要不要写在封装的方法中？从前面的代码可以看出，测试的断言点是一样的。不过，笔者更倾向于把断言写在每一条测试用例里面，
因为很多时候就算操作步骤是一样的，断言点也不完全一样。例如，登录功能的测试用例，虽然操作步骤相同，但是用户名为空和密码为空，这两条测试用例的提示信息可能显示在
不同的位置，所以获取提示信息的定位方法是不一样的，因此断言也就不完全一样了。另外，从设计的角度来看，断言写在每一个测试用例中也会更加清晰。

'''
import unittest
from time import sleep
from selenium import webdriver


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

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
