'''
给你一个由 n 个整数组成的数组nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]] ：

0 <= a, b, c, d< n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        if n<4:
            return []
        nums.sort()
        res=[]
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]: continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[n-3]+nums[n-2]+nums[n-1]<target:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j - 1]: continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                left=j+1
                right=n-1
                while left<right:
                    sum=nums[i] + nums[j] + nums[left] + nums[right]
                    if sum==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        right-=1
                    elif sum>target:
                        right-=1
                    else:
                        left+=1
        return res


