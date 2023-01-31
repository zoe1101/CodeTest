#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
import allure

class TestCase:
    def test_01(self):
        print('---用例01---')
        assert 1
    def test_02(self):
        print('---用例02---')
        assert 1

pytest.main(['test_allure.py', '--alluredir=report'])

'''
1.在控制台第一次运行方式，生成数据：pytest test_allure.py   --alluredir report
2.
    方法1：在控制台第二次把数据生成报告：allure generate report/ -o report/html --clean           生成报告文件
    方法2：或者直接生成web网页报告：allure serve report
'''