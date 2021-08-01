'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路：从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。
'''
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        row=0
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                row+=1
            else:
                col-=1
        return False


if __name__ == '__main__':
    while True:
        array =[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
        target = int(input('请输入target数：'))
        print(Solution().findNumberIn2DArray(array,target))