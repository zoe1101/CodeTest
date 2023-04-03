# coding:utf-8
import requests


class Requests_Handle:
    def __init__(self, host):
        self.host = host

    def send_method(self, method, url, headers=None, params=None, data=None, files=None):
        url = self.host + url
        if method.lower() == "post" and params is not None and data is None:
            raise ValueError("post请求传参是data,请检查数据参数")
        global response
        if params and not data:
            if isinstance(params, dict):
                response = requests.request(method, url, params=params, headers=headers)
                return response.json()
            else:
                print("params should be dict type!")
        elif not params:
            if files:
                response = requests.post(url, data, headers=headers, files=files)
            elif files and data:
                response = requests.request(method, url, json=data, headers=headers, files=files)
            elif not files and data:
                response = requests.request(method, url, json=data, headers=headers)
            else:
                response = requests.request(method, url, headers=headers)
            return response.json()
        else:
            print("request maybe is wrong.")


if __name__ == '__main__':
    req = Requests_Handle(host="https://postman-echo.com")
    resp = req.send_method('get', '/get', params={"foo1": "bar1", "foo2": "bar2"})
    print(resp)
