'''
给定一个包含 n 个整数的数组nums，判断nums中是否存在三个元素a ，b ，c ，使得a + b + c = 0 ？请找出所有和为 0 且不重复的三元组。

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums)<3:
            return res
        nums.sort()
        n=len(nums)
        #枚举每一位，然后之后后面的求twoSum，只不过target需要减去枚举的那一位
        for i in range(n-2):
            if i!=0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=n-1
            while left<right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum==0:
                    res.append([nums[i],nums[left],nums[right]])
                    #剪枝，去掉 重复结果,把跟nums[left] 、nums[right] 相同的数去掉 后 在移动左右指针
                    while left < right and nums[left] == nums[left + 1]:
                        left+=1
                    while (left < right and nums[right] == nums[right - 1]):
                        right-=1
                    left+=1
                    right-=1
                elif curSum<0:
                    left+=1
                else:
                    right-=1
        return res
