import pytest
# Faker结合pytest使用

@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return 12345

def test_something(faker):
    # The faker fixture will use the session seed value
    pass

def test_something_else(faker, faker_seed):
    # The faker fixture will use the seed value 12345
    pass


if __name__ == '__main__':
    pytest.main(['-vs','Faker结合pytest使用.py'])