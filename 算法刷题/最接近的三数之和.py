'''
给定一个包括n 个整数的数组nums和 一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        res = float('inf')
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==target:
                    return sum
                elif sum>target:
                    right-=1
                else:
                    left+=1

                res=sum if abs(target-sum)<abs(target-res) else res
        return res



