import os
import sys
import allure
import pytest

'''当条件为True则跳过执行'''
@allure.feature("test_skipif")
@pytest.mark.skipif("windows" in sys.platform,reason="如果操作系统是windows则跳过执行")
def test_skipif():
    print("操作系统是windows，test_skipif()函数跳过执行")

# --clean-alluredir:每次执行前清空数据，这样在生成的报告中就不会追加，只显示当前执行的用例
pytest.main(['-s', '-q','skipif_demo.py','--clean-alluredir','--alluredir=result'])
os.system(r"allure serve result")
