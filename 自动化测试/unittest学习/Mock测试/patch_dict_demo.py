from unittest.mock import patch
'''
patch.dict() ������һ���������������ֵ��ֵ�������Խ���ʱ���ֵ�ᱻ�ָ���ԭʼ״̬����������װ��������װ�����������Ĺ���
'''
foo = {'key': 'value'}
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}
    print(foo)

print(foo)
