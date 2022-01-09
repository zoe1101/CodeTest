'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

思路：利用双指针将非0元素前移最后再将其余元素赋0
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n<2:
            return
        slow=0
        for fast in range(n):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        for i in range(slow,n):
            nums[i]=0
        print(nums)

if __name__ == '__main__':
    a=[0,1,0,3,12]
    Solution().moveZeroes(a)
