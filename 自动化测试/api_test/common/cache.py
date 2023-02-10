# -*- coding: utf-8 -*-
"""
缓存类
"""
import typing as t
from collections import UserDict
import pytest


class CachePool(UserDict):
    """全局变量池"""

    def get(self, key: t.Text, default=None) -> t.Any:
        return self.data.get(key, default)

    def set(self, key: t.Text, value: t.Any = None) -> None:
        self.data.setdefault(key, value)
        '''
        UserDict.data.setdefault:
            如果关键字不在字典中，则使用默认值插入关键字。
            如果key在字典中，则返回key的值，否则返回默认值。
        '''
    def new_set(self, key: t.Text, value: t.Any = None) -> None:
        if value:
            self.data[key] = value
    def has(self, key: t.Text) -> bool:
        return key in self.data

    def __len__(self) -> int:
        return len(self.data)

    def __bool__(self) -> bool:
        return bool(self.data)


cache = CachePool()

if __name__ == '__main__':
    v = 1
    cache.set('a', v)
    print(cache.get('a'))
    cache.set('a', 12)
    print(cache.get('a'))
    # print(len(cache))
