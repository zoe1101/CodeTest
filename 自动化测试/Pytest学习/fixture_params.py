import pytest


@pytest.fixture(scope='function', params=['a', 'b', 'c'])
def my_fixture(request):
    return request.param


class TestDemo:
    def test_01(self):
        assert 1 == 2

    def test_02(self, my_fixture):
        assert 1 == 1


pytest.main(['-vs','fixture_params.py'])
