import unittest
from unittest import mock
import mock_obj

#
# def test1():
#     mock_multiple = mock.patch.multiple(mock_obj, funa=mock.DEFAULT, funb=mock.DEFAULT)
#     mock_multiple.start()
#     mock_multiple['funa'].return_value = 10
#     mock_multiple['funb'].return_value = 20
#     result1 = mock_obj.funa()
#     result2 = mock_obj.funb()
#     mock_multiple.stop()
#     assert result1 == 10
#     assert result2 == 20


def mock_side_effect():
    return 21


# 装饰器方式调用
@mock.patch.multiple(mock_obj, funa=mock.DEFAULT, funb=mock.DEFAULT)
def test2(funa, funb):
    '''
    该方法并不推荐使用，因为如果需要一次mock两个对象完全可以用装饰器@mock.path()的方式，比起该方法更加直观和简洁。
    :param funa:
    :param funb:
    :return:
    '''
    funa.side_effect = mock_side_effect
    funb.return_value = 22
    result1 = mock_obj.funa()
    result2 = mock_obj.funb()
    assert result1 == 21
    assert result2 == 22


# 上下文管理器方式调用
def test3():
    with mock.patch.multiple(mock_obj, funa=mock.DEFAULT, funb=mock.DEFAULT) as mock_multiple:
        mock_multiple['funa'].return_value = 41
        mock_multiple['funb'].return_value = 42
        result1 = mock_obj.funa()
        result2 = mock_obj.funb()
        assert result1 == 41
        assert result2 == 42


if __name__ == '__main__':
    unittest.main(['-vs'])
