"""
pytest处理
"""
import typing as t
import yaml
import pytest
from requests import Response
from common.cache import cache
from common.json_deal import dumps, loads
from common.request_deal import HttpRequest
from common.regular import findalls, sub_var
from common.result import get_result, check_results
from common.exceptions import YamlException, RequestException
from utils.logger import logger


def pytest_collect_file(parent, path):
    if path.ext in (".yaml", ".yml") and path.basename.startswith("test"):
        return YamlFile.from_parent(parent, fspath=path)


def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('unicode_escape').decode('utf-8')
        item._nodeid = item.nodeid.encode('unicode_escape').decode('utf-8')


class YamlFile(pytest.File):
    '''继承pytest.File '''

    def collect(self):
        raw = yaml.safe_load(self.fspath.open(encoding='utf-8'))
        if not any(k.startswith('test') for k in raw.keys()):
            raise YamlException("{}yaml non test found".format(self.fspath))
        if variable := raw.get('variable'):
            for k, v in variable.items():
                cache.set(k, v)  # 放入缓存
        if config := raw.get('config'):
            keys = findalls(dumps(config))
            config = loads(sub_var({k: cache.get(k)
                                    for k in keys}, dumps(config)))
            for k, v in config.items():
                cache.set(k, v)  # 放入缓存
        logger.warning(f'conftest:{cache}')
        if tests := raw.get('tests'):
            for name, spec in tests.items():
                yield YamlTest.from_parent(self,
                                           name=spec.get(
                                               'description') or name,
                                           spec=spec)


class YamlTest(pytest.Item):
    def __init__(self, name, parent, spec):
        super(YamlTest, self).__init__(name, parent)
        self.spec = spec
        self.request = HttpRequest(exception=(RequestException, Exception))

    def runtest(self):
        """Some custom test execution (dumb example follows).
        运行案例
        """
        if self.spec.get('is_run', True):
            r = self.request.send_request(**self.spec)
            self.response_handle(r, self.spec.get(
                'Validate'), self.spec.get('Extract'))
        else:
            pytest.skip(f'该案例已被跳过执行！')

    def response_handle(self, r: Response, validate: t.Dict, extract: t.List):
        """Handling of responses"""
        if validate:  # 验证结果
            check_results(r, validate)
        if extract:  # 提取数据
            get_result(r, extract)

    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        logger.critical(excinfo.value)
        logger.critical(excinfo.traceback[-6:-1])

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.name}"


if __name__ == '__main__':
    pytest.main()
