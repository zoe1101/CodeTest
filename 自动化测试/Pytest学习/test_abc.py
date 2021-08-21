# file_name: test_abc.py
import pytest # 引入pytest包
import pytest

def func(x):
    return x + 1
def test_answer():
    assert func(3) == 5

if __name__ == '__main__':
       pytest.main(["-s","test_abc.py"]) # 调用pytest的main函数执行测试