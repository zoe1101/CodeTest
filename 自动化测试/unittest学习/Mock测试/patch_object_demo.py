import unittest
from unittest import mock
import mock_obj


def test1():
    mock_get_sum = mock.patch.object(target=mock_obj, attribute='get_sum', return_value=20)
    mock_get_sum.start()
    result = mock_obj.get_sum()
    mock_get_sum.stop()
    assert result == 20


def mock_side_effect():
    return 30


# 装饰器方式调用
@mock.patch.object(mock_obj, 'get_sum')
def test2(mock_get_sum):
    mock_get_sum.side_effect = mock_side_effect
    result = mock_obj.get_sum()
    assert result == 30


# 上下文管理器方式调用
def test3():
    with mock.patch.object(mock_obj, 'get_sum', new=40):
        result = mock_obj.get_sum
        assert result == 40


if __name__ == '__main__':
    unittest.main(['-vs'])
