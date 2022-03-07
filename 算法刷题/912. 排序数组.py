'''
给你一个整数数组 nums，请你将该数组升序排列。



示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
'''
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums, start, end):
            if start>=end:
                return
            pivot_idx = random.randint(start, end)  # 随机选择pivot基准元素
            nums[start], nums[pivot_idx] = nums[pivot_idx], nums[start]  # pivot放置到最左边
            pivot = nums[start]
            left=start
            right=end
            while left<right:
                while right>left and nums[right]>=pivot:
                    right-=1
                while right>left and nums[left]<=pivot:
                    left+=1
                if right>left:
                    nums[left],nums[right]=nums[right],nums[left]
            nums[start],nums[left]=nums[left],nums[start]
            print(nums)
            quicksort(nums,start,left-1)
            quicksort(nums,left+1,end)
        quicksort(nums,0,len(nums)-1)
        return nums

#测试
data_test=[5,1,1,2,0,0]
sorted_list = Solution().sortArray(data_test)
print(sorted_list)