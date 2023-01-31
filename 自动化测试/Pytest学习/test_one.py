#!/usr/bin/env python
# !coding:utf-8
import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize('a,b,expect', [
    [1, 1, 2],
    [2, 2, 4],
    [3, 3, 6],
    [4, 4, 8],
    [5, 5, 10]
])
def test_add_list(a, b, expect):
    assert add(a, b) == expect


@pytest.mark.parametrize('a,b,expect', [
    (1, 1, 2),
    (2, 2, 4),
    (3, 3, 6),
    (4, 4, 8),
    (5, 5, 10)
])
def test_add_tuple(a, b, expect):
    assert add(a, b) == expect


@pytest.mark.parametrize('data', [
    {'a': 1, 'b': 1, 'expect': 2},
    {'a': 5, 'b': 5, 'expect': 10}
])
def test_add_dict(data):
    assert add(data['a'], data['b']) == data['expect']


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_one.py"])