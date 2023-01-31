import os

import allure
import pytest

'''
xfails：功能未实现或者有Bug尚未修复，当测试通过时尽管会失败，它是一个xpass，将在测试摘要中报告。
'''
@allure.feature('test_xfail_expected_failure')
@pytest.mark.xfail(reason='该功能尚未实现')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    print("该功能尚未实现")
    assert False

@allure.feature('test_xfail_unexpected_pass')
@pytest.mark.xfail(reason='该Bug尚未修复')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    print("该Bug尚未修复")
    assert True


pytest.main(['-s', '-q','xfail_demo.py','--clean-alluredir','--alluredir=result'])
# os.system(r"allure generate -c -o result")
os.system(r"allure serve result")
