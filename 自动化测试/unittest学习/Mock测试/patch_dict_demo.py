from unittest.mock import patch
'''
patch.dict() 用于在一个作用域中设置字典的值，当测试结束时，字典会被恢复到原始状态。可以用作装饰器、类装饰器或上下文管理
'''
foo = {'key': 'value'}
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}
    print(foo)

print(foo)
