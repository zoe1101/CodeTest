'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if exponent==0:
            return 1
        elif base==0:
            return 0
        res=1
        abs_exponent=abs(exponent)
        while abs_exponent>0:
            res*=base
            abs_exponent-=1
        if exponent<0:
            res=1/res
        return res

