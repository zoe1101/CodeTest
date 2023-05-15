import os

import pytest


def test_spy_listdir(mocker):
    '''
    在所有情况下，mocker.spy对象的行为都与原始方法完全相同，只是spy还跟踪函数/方法调用、返回值和引发的异常。
    :param mocker:
    :return:
    '''
    mock_listdir = mocker.spy(os, 'getcwd')
    os.getcwd()
    assert mock_listdir.called


def foo(param):
    param('foo', 'bar')


def test_stub(mocker):
    '''
    存根是一个模拟对象，它接受任何参数，对测试调用非常有用。
    stub可以模拟测试对象中的属性，如可以模拟成测试对象中的变量，函数等。将stub实例传入测试对象中，可以获得测试对象内部执行的过程。所以：
    Stub 可以跟踪和测试对象的交互，使用在回调函数中十分有效。
    :param mocker:
    :return:
    '''
    # 模拟成foo中的一个函数
    stub = mocker.stub(name='on_something_stub')

    foo(stub)

    # 测试foo中这个函数的调用参数是否正确
    stub.assert_called_once_with('foo', 'bar')


if __name__ == '__main__':
    pytest.main(['-vs'])