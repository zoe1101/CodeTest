'''
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]


思路：双指针法


'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        while i<j:
            s=nums[i]+nums[j]
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [nums[i],nums[j]]
        return []