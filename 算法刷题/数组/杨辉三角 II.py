'''
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:

输入: rowIndex = 3
输出: [1,3,3,1]


'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        思路： 在杨辉三角中，每个数是它左上方和右上方的数的和
        方法： 1. 每一行等于上一行前后错位后之和
              2. O(k)的空间复杂度，防止覆盖需要倒序遍历
                13310
               +01331
                14641
        """
        row=[0]*(rowIndex+1)
        for i in range(0,rowIndex+1):
            for j in range(i,-1,-1): #防止覆盖需要倒序遍历
                if j==0 or j==i:
                    row[j]=1
                else:
                    row[j]=row[j]+row[j-1]
        return row
