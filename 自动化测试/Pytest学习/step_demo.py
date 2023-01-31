import os
import allure
import pytest

@allure.step("步骤二")
def passing_step():
    pass


@allure.step("步骤三")
def step_with_nested_steps():
    nested_step()


@allure.step("步骤四")
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("步骤五")
def nested_step_with_arguments(arg1, arg2):
    pass


@allure.step("步骤一")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()

pytest.main(['-s', '-q', 'step_demo.py', '--clean-alluredir', '--alluredir=result'])
os.system(r"allure serve result")
