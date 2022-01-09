'''
给定一个非负整数numRows，生成「杨辉三角」的前numRows行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。



示例 1:
输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

思路： 在杨辉三角中，每个数是它左上方和右上方的数的和
方法： 每一行等于上一行前后错位后之和
        13310
       +01331
        14641

'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            row=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(res[i-1][j-1]+res[i-1][j])
            res.append(row)
        return res