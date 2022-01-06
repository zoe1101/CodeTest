'''
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]


思路：
// 首先, 对角线遍历. x+y是固定值
// 当 x+y 为奇数时对角线上的数据正序输出，为偶数时倒序输出。
// 细节在于起始值, 和行列限制
'''
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = list()
        m = len(mat) - 1
        n = len(mat[0]) - 1
        x, y = 0, 0  # 当前坐标
        for i in range(m + n + 1):  # 0<=x+y<=m+n
            if i % 2 == 0:  # x+y为偶数，逆序遍历
                for j in range(x, i - y - 1, -1):
                    res.append(mat[j][i - j])
            else:  # x+y为奇数，正序遍历
                for j in range(y, i - x - 1, -1):
                    res.append(mat[i - j][j])
            x = m if x >= m else x + 1
            y = n if y >= n else y + 1
        return res
