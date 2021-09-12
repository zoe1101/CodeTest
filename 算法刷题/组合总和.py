'''
给定一个无重复元素的正整数数组candidates和一个正整数target，找出candidates中所有可以使数字和为目标数target的唯一组合。
candidates中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。
对于给定的输入，保证和为target 的唯一组合数少于 150 个。

示例1：
输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]

回溯算法
'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target==0:
                res.append(path)
                return
            for i in range(begin,size):
                residue =target-candidates[i]
                if residue<0:
                    break
                dfs(candidates,i,size,path+[candidates[i]],res,residue)
        size=len(candidates)
        if size==0:
            return []
        candidates.sort()
        path=[]  #暂存当前路径
        res=[]
        dfs(candidates,0,size,path,res,target)
        return res