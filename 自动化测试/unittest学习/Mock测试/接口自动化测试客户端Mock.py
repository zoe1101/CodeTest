'''
通过代码去模拟假的接口返回数据（访问真实接口的过程就可以省略）

举个栗子：要测试请求接口visit接口，实际上开发还没完成开发工作，我们先编写测试用例，数据都先准备空的，然后可以运行通过，等开发好接口以后，再把相应内容如info中的数据，实际结果等修改后运行
'''

import requests
import unittest
from unittest import TestCase, mock
from mock import Mock

class TestRegister(unittest.TestCase):
    def test_register_01(self):
        '''步骤：
        1.准备测试数据
        2.发送接口请求，得到实际结果
        3.预期结果和实际结果的断言
        '''

        # 1.准备测试数据
        url = 'http://api.lemonban.com:8766/futureloan/member/register'
        method = 'post'
        headers = {'X-Lemonban-Media-Type': 'lemonban.v2'}
        json_data = {"mobile_phone": "", "pwd": "12345678"}
        expected = {
            "code": 1,
            "msg": "手机号为空",
            "data": None,
            "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
        }
        # 2.发送接口请求，得到实际结果
        # 因为执行了Mock,所以就不会执行请求真实的接口了
        requests.request = Mock(return_value=expected)
        response = requests.request(method=method, url=url, headers=headers, json=json_data)
        # mock返回的是expected的内容，因此是dict,所以实际结果要把之前代码上的.json去掉
        actual = response
        # 3.预期结果和实际结果的断言
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
