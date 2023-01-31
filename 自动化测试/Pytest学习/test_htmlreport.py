import pytest


@pytest.mark.repeat(2)
def test_case1():
    print("执行测试用例1")
    assert 1 + 1 == 2


def test_case2():
    print("执行测试用例2")
    assert 1 + 3 == 6


'''
命令行执行时配置 --html参数
pytest --html=report.html -s test_htmlreport.py
'''

pytest.main(['--html=html_report.html', '-s'])
