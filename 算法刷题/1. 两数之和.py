'''
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}  ##记录元素本身及其索引位置
        for i,n in enumerate(nums):
            if target-n in dic:
                return [dic[target-n],i]
            dic[n]=i
        return []