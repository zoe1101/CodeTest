import pytest
def f():
    return 3


def test_function():
    ''' 普通断言'''
    assert f() == 4


def test_zero_division():
    '''
    预期异常的断言.为了编写有关引发异常的断言，您可以使用 pytest.raises() 作为上下文管理器.
    :return:
    '''
    with pytest.raises(ZeroDivisionError):
        1 / 0

pytest.main([])