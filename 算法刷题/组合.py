'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案。

示例 1：
输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(n,k,begin,path,res):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(begin,n+1):
                path.append(i)
                dfs(n,k,i+1,path,res)
                path.pop()

            return
        res = []
        if n <= 0 or k <= 0 or k > n:
            return res
        path=[]
        dfs(n,k,1,path,res)
        return res

