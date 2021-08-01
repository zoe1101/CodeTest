'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).

思路：如果数组里所有的整数都是负数，那么选择最大的数即可，因为越累加越小。
正负数都有的情况，需要两个变量，一个是global_max,从全局来看，每次最大的是什么组合，另一个是local_max，和global_max相比，更新global_max。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        res=0
        if max(array)<=0:  #如果数组里所有的整数都是负数，那么选择最大的数即可，因为越累加越小。
            return max(array)
        local_max, global_max = 0, 0
        for i in array:
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
        return global_max