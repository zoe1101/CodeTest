'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

思路：从左下角元素往上查找，右边元素是比这个元素大，上边是的元素比这个元素小。于是，target比这个元素小就往上找，比这个元素大就往右找。如果出了边界，则说明二维数组中不存在target元素。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array)==0 or len(array[0])==0:
            return False
        rows=len(array)
        cols=len(array[0])
        i=rows-1
        j=0
        while i>=0 and j<cols:
            if target<array[i][j]: #查找的元素较小，往上找
                i=i-1
            elif target>array[i][j]: #查找元素较大，往右找
                j=j+1
            else:  #找到了
                return True
        return False


if __name__ == '__main__':
    while True:
        array =[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
        target = int(input('请输入target数：'))
        print(Solution().Find(target,array))