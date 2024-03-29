'''
给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组[4,-1,2,1] 的和最大，为6 。

输入：nums = [1]
输出：1

'''
from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        res=nums[0]
        cursum=nums[0]
        for i in range(1,n):
            cursum=cursum+nums[i] if cursum>0 else nums[i]
            res=max(res,cursum)
        return res


    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)