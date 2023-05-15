import requests
import unittest
from unittest import TestCase, mock

class TestHTTP(TestCase):
    def test_http_success(self):
        # 模拟 HTTP 请求成功的情况
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = { 'message': 'Hello, World!' }

            response = requests.get('<http://example.com/>')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['message'], 'Hello, World!')

    def test_http_failure(self):
        # 模拟 HTTP 请求失败的情况
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404

            response = requests.get('<http://example.com/>')
            self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()