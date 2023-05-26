import pytest
import requests

host = 'http://erp2.hzb-it.com'


@pytest.fixture(scope="session")
def get_token():
    '''
    获取登录时的token
    :return:
    '''
    url = host + '/app/common/login'
    resp = requests.post(url, data={'username': 'admin', 'password': '123'})
    assert resp.status_code == 200
    token = resp.json()['data']
    return token


def test_position_list(get_token):
    '''
    查询组织人员
    :param get_token:
    :return:
    '''
    url = host + '/app/common/position/list'
    headers = {'access-token': get_token}
    resp = requests.get(url, headers=headers,
                        params={'name': 'pm', 'page': 1, 'pageSize': '30'},
                        ).json()
    assert resp['records'][0]['name'] == 'pm'


if __name__ == '__main__':
    pytest.main(['-vs', '参数关联_先登录再操作.py'])
