'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

 

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelection(left, right):
            i = left
            j = right
            while i < j:
                while i < j and nums[j] >= nums[left]:  ##大于基准的数
                    j -= 1
                while i < j and nums[i] <= nums[left]:  ##小于基准的数
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]  # 交换左右指针元素
            nums[left], nums[i] = nums[i], nums[left]  # 将基准与左指针元素交换
            return i

        n = len(nums)
        left, right = 0, n - 1
        target = n - k  # 正序第几大的数
        while left < right:
            mid = quickSelection(left, right)
            if mid == target:
                return nums[mid]
            if mid < target:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
