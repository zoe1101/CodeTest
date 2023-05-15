from unittest import mock
import unittest
from .mock_obj import get_sum

def test1():
    get_sum = mock.Mock(return_value=20)
    # 等同于
    # get_sum = mock.Mock()
    # get_sum.return_value = 20

    result = get_sum()
    assert result == 20


def mock_side_effect():
    return 30


def test2():
    '''
    当 return_value 和 side_effect 同时设置时，会返回side_effect的结果。
    :return:
    '''
    get_sum = mock.Mock(return_value=20, side_effect=mock_side_effect)
    result = get_sum()
    assert result == mock_side_effect()


if __name__ == '__main__':
    unittest.main(['-vs'])
