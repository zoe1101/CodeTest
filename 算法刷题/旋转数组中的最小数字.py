'''
题目描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路：二分查找
'''

# -*- coding:utf-8 -*-
import math


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while l < r:
            mid =int((l + r) / 2)
            if rotateArray[mid] > rotateArray[r]: ## 左边是有序的
                l = mid + 1
            else: ##右边是有序的
                r = mid
        return rotateArray[l]

if __name__ == '__main__':
    rotateArray=[3,4,5,1,2]
    print(Solution().minNumberInRotateArray(rotateArray))
