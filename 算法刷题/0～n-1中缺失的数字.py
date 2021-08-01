'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2


思路：二分法
使用二分法查找 “右子数组的首位元素” 。
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            mid=(i+j)>>1
            if nums[mid]==mid:
                i=mid+1
            else:
                j=mid-1
        return i