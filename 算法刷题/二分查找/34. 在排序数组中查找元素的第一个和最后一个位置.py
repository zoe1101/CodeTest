'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

进阶：

你可以设计并实现时间复杂度为O(logs n)的算法解决此问题吗？


示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right:  # 寻找左边界
            mid = (left + right) >> 1
            if nums[mid] < target:
                left += 1
            elif nums[mid] == target:
                right = mid
            else:
                right = mid - 1
        if nums[left] != target:
            return [-1, -1]
        left2 = left
        right2 = n - 1
        while left2 <= right2:  # 已知左边界后直接从左边到数列尾寻找有边界
            mid = (left2 + right2) >> 1
            if nums[mid] == target:
                left2 = mid + 1
            elif nums[mid] > target:
                right2 = mid - 1
        return [left, right2]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
