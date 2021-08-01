'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：

思路：
n = 1: f(n) = 1; n=2 : f(n) = 2;
假设到了n，那么上一步就有两种情况，在n-1的时候，竖放一个矩形，或着是在n-2时，横放两个矩形（这里不能竖放两个矩形，因为放一个就变成了n-1，那样情况就重复了），所以总数是f(n)=f(n-1)+f(n-2)。时间复杂度O(n)。和跳台阶题一样。
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number<=0:
            return 0
        if number==1 or number==2:
            return number
        res=[0,1,2]
        for i in range(3,number+1):
            res.append(res[i-2]+res[i-1])
        return res[number]