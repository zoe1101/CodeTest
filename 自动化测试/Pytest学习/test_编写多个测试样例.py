import pytest
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

if __name__ == '__main__':
       pytest.main(["-s","test_编写多个测试样例.py"]) # 调用pytest的main函数执行测试