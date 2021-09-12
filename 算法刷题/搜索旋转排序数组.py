'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n==0:
            return -1
        left,right=0,n-1
        while left<=right:
            mid=(left+right)>>1
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:  #左侧有序
                if target>=nums[left] and target<nums[mid]: #目标值在左侧
                    right=mid-1
                else:#目标值在右侧
                    left=mid+1
            else:#右侧有序
                if target > nums[mid] and target <=nums[right]:  # 目标值在右侧
                    left = mid + 1
                else:  # 目标值在左侧
                    right = mid - 1
        return -1

