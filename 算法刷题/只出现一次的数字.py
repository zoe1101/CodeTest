'''
给你一个整数数组nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

示例 1：
输入：nums = [2,2,3,2]
输出：3

思路：位运算
一个整数无非是由 32 个 0 和 1 组成的，那么我们可以将数组中所有数字的同一位置的数位相加。
将出现三次的数字单独拿出来，那么这些出现了三次的数字，任意的某一位数位置之和能被三整除
理解下面两句话：
因此如果数组中所有数字的第 i 位数位相加之和能被三整除，那么只出现一次的数字的第 i 数位一定是零。
相反，如果数组中所有数字的第 i 位数位相加之和能被三除余一，那么只出现一次的数的第 i 位数一定是 1
这样只出现一次的任意第 i 个数为可以由数组中所有数字的第 i 位数字和推算出来。
当我们知道了一个整数任意的某一位是 0 和 1 之后，也就知道了这个整数的数值。


举一反三
输入一个整数数组，数组中只有一个数字出现了 m 次，其他数字都出现了 n 次。请你找出那个唯一出现 m 的数字，那么假设 m 不能被 n 整除。
分析：这道题可以由第一道题举一反三而来，如果数组中所有数字的第 i 位数相加之和能被 n 整除，那么出现 m 次的数的第 i 数位一定是零，否则出现 m 次的数的第 i 位数一定是1。


位运算遇到负数不好处理
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        先排序，在筛选比较
        :param nums:
        :return:
        '''
        nums.sort()
        if len(nums) < 2 or nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        for i in range(2, len(nums) - 1):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
    def singleNumber1(self, nums: List[int]) -> int:
        '''位运算遇到负数时失效'''
        bitSum=[0]*32
        for n in nums:
            for i in range(32):
                bitSum[i]+=(n>>(31-i))&1
        print(bitSum)
        res=0
        for i in range(32):
            res = (res << 1) + bitSum[i] % 3
        return res

if __name__ == '__main__':
    print(Solution().singleNumber([2,2,2,5,5,-3,5]))
