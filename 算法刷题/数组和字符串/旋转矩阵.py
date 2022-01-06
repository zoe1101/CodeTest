'''
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

不占用额外内存空间能否做到？


示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

本题与主站 48 题相同：https://leetcode-cn.com/problems/rotate-image/


思路：通过翻转实现
总结：
如果是顺时针旋转90°，一定是先水平翻转(-)，再主对角线翻转（\）
如果是逆时针旋转90°，一定是先水平翻转(-)，再副对角线翻转(/)


作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/clpgd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #水平翻转
        for i in range(n//2):
            for j in range(n):
                matrix[i][j],matrix[n-i-1][j]=matrix[n-i-1][j],matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
