# -*- coding: utf-8 -*-
"""
requests二次封装
"""
import re
import typing as t
import allure
import urllib3
from requests import Session, Response

from common import exceptions
from common.cache import cache
from common.json_deal import loads, dumps
from common.regular import sub_var, findalls
from utils.logger import logger

urllib3.disable_warnings()


class HttpRequest(Session):
    """requests方法二次封装"""

    def __init__(self, *args: t.Union[t.Set, t.List], **kwargs: t.Dict[t.Text, t.Any]):
        super(HttpRequest, self).__init__()
        self.exception = kwargs.get("exception", Exception)

    @staticmethod
    def check_url(base_url: str, url: str) -> str:
        """ 拼接base_url 和 url 地址"""
        if re.compile(r"(http)(s?)(://)").match(url):
            return url
        elif base_url:
            if re.compile(r"(http)(s?)(://)").match(base_url):
                return f"{base_url.rstrip('/')}/{url.lstrip('/')}"
            else:
                raise exceptions.ParserError("base url do yo mean http:// or https://!")
        else:
            raise exceptions.ParserError("url invalid or base url missed!")

    def send_request(self, **kwargs: t.Dict[t.Text, t.Any]) -> Response:
        """发送请求
        :param is_run: 是否执行
        :param method: 发送方法
        :param route: 发送路径
        optional 可选参数
        :param extract: 要提取的值
        :param params: 发送参数-"GET"
        :param data: 发送表单-"POST"
        :param json: 发送json-"post"
        :param headers: 头文件
        :param cookies: 验证字典
        :param files: 上传文件,字典：类似文件的对象``
        :param timeout: 等待服务器发送的时间
        :param auth: 基本/摘要/自定义HTTP身份验证
        :param allow_redirects: 允许重定向，默认为True
        :type bool
        :param proxies: 字典映射协议或协议和代理URL的主机名。
        :param stream: 是否立即下载响应内容。默认为“False”。
        :type bool
        :param verify: （可选）一个布尔值，在这种情况下，它控制是否验证服务器的TLS证书或字符串，在这种情况下，它必须是路径到一个CA包使用。默认为“True”。
        :type bool
        :param cert: 如果是字符串，则为ssl客户端证书文件（.pem）的路径
        :return: request响应
        """
        try:
            logger.info("request data: {}".format(kwargs))
            method = kwargs.get('method', 'GET').upper()
            if kwargs.get('host'):  # 对于个别host不一致的，在案例中设置自己的host
                host = kwargs.get('host')
            else:
                host = cache.get('baseurl')
            url = self.check_url(host, kwargs.get('route'))
            logger.info("Request Url: {}".format(url))
            logger.info("Request Method: {}".format(method))
            kwargs_str = dumps(kwargs)
            if is_sub := findalls(kwargs_str):
                kwargs = loads(sub_var(is_sub, kwargs_str))
            logger.info("Request Data: {}".format(kwargs))
            request_data = HttpRequest.mergedict(kwargs.get('RequestData'),
                                                 headers=cache.get('headers'),
                                                 timeout=cache.get('timeout'))
            response = self.dispatch(method, url, **request_data)
            description_html = f"""
            <font color=red>请求方法:</font>{method}<br/>
            <font color=red>请求地址:</font>{url}<br/>
            <font color=red>请求头:</font>{str(response.headers)}<br/>
            <font color=red>请求参数:</font>{dumps(kwargs, ensure_ascii=False)}<br/>
            <font color=red>响应状态码:</font>{str(response.status_code)}<br/>
            <font color=red>响应时间:</font>{str(response.elapsed.total_seconds())}<br/>
            """
            allure.dynamic.description_html(description_html)
            logger.info("Request Result: {}{}".format(response, response.text))
            return response
        except self.exception as e:
            logger.exception(format(e))
            raise e

    def dispatch(self, method: t.Text, *args: t.Union[t.List, t.Tuple], **kwargs: t.Dict) -> Response:
        """请求分发"""
        handler = getattr(self, method.lower())
        return handler(*args, **kwargs)

    @staticmethod
    def mergedict(args: t.Dict, **kwargs: t.Dict):
        """合并字典"""
        for k, v in args.items():
            if k in kwargs:
                kwargs[k] = {**args[k], **kwargs.pop(k)}
        args.update(kwargs)
        return args
