# -*- coding: utf-8 -*-


"""
response响应处理
"""
import re
import typing as t
import pytest
import allure
from requests import Response
from common.cache import cache
from common.regular import re, get_var
from utils.logger import logger
from common import validate_deal, extract


def get_result(r: Response, extract: t.List) -> None:
    """获取值"""
    for key in extract:
        value = get_var(key, r.text)
        logger.debug("正则提取结果值：{}={}".format(key, value))
        cache.set(key, value)
        pytest.assume(key in cache)
    with allure.step("提取返回结果中的值"):
        for key in extract:
            allure.attach(name="提取%s" % key, body=cache.get(key))

def check_results(response: Response, validate: t.List) -> None:
    for check in validate:
        for check_type, check_value in check.items():
            actual_value = extract.extract_by_object(response, check_value[0])  # 实际结果
            expect_value = check_value[1]  # 期望结果
            if check_type in ["eq", "equals", "equal"]:
                validate_deal.equals(actual_value, expect_value)
            elif check_type in ["lt", "less_than"]:
                validate_deal.less_than(actual_value, expect_value)
            elif check_type in ["le", "less_or_equals"]:
                validate_deal.less_than_or_equals(actual_value, expect_value)
            elif check_type in ["gt", "greater_than"]:
                validate_deal.greater_than(actual_value, expect_value)
            elif check_type in ["ne", "not_equal"]:
                validate_deal.not_equals(actual_value, expect_value)
            elif check_type in ["str_eq", "string_equals"]:
                validate_deal.string_equals(actual_value, expect_value)
            elif check_type in ["len_eq", "length_equal"]:
                validate_deal.length_equals(actual_value, expect_value)
            elif check_type in ["len_gt", "length_greater_than"]:
                validate_deal.length_greater_than(actual_value, expect_value)
            elif check_type in ["len_ge", "length_greater_or_equals"]:
                validate_deal.length_greater_than_or_equals(actual_value, expect_value)
            elif check_type in ["len_lt", "length_less_than"]:
                validate_deal.length_less_than(actual_value, expect_value)
            elif check_type in ["len_le", "length_less_or_equals"]:
                validate_deal.length_less_than_or_equals(actual_value, expect_value)
            elif check_type in ["contains"]:
                validate_deal.contains(actual_value, expect_value)
            else:
                if hasattr(validate, check_type):
                    getattr(validate, check_type)(actual_value, expect_value)
                else:
                    print(f'{check_type}  not valid check type')
            # 在allure中打印预期，实际结果
            with allure.step(f"校验路径：{check_value[0]}\t校验方式：{check_type}"):
                allure.attach(name='预期结果', body=str(expect_value))
                allure.attach(name='实际结果', body=str(actual_value))

def check_results1(r: Response, validate: t.Dict) -> None:
    """检查运行结果"""
    expectcode = validate.get('expectcode')
    resultcheck = validate.get('resultcheck')
    regularcheck = validate.get('regularcheck')
    if expectcode:
        with allure.step("校验返回响应码"):
            allure.attach(name='预期响应码', body=str(expectcode))
            allure.attach(name='实际响应码', body=str(r.status_code))
        pytest.assume(expectcode == r.status_code)
    if resultcheck:
        with allure.step("校验响应预期值"):
            allure.attach(name='预期值', body=str(resultcheck))
            allure.attach(name='实际值', body=r.text)
        pytest.assume(resultcheck in r.text)
    if regularcheck:
        with allure.step("正则校验返回结果"):
            allure.attach(name='预期正则', body=regularcheck)
            allure.attach(name='响应值', body=str(
                re.findall(regularcheck, r.text)))
        pytest.assume(re.findall(regularcheck, r.text))