'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(level):
            if level==n:
                res.append(nums[:])
            for i in range(level,n):
                nums[i],nums[level]=nums[level],nums[i] #修改当前节点状态
                backtrack(level+1) #递归子节点
                nums[i], nums[level] = nums[level], nums[i] #回改当前节点状态

        res = []
        n=len(nums)
        backtrack(0)
        return res
if __name__ == '__main__':
    nums = [1, 2, 3]
    print(nums[:],nums)
    print(Solution().permute(nums))