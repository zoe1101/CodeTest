'''
给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/c0w4r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

思路：滑动窗口
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right=0,0
        sum=0
        n=len(nums)
        cnt=n+1  ##默认长度最大
        while right<n:
            sum+=nums[right]
            while sum>=target:
                cnt=min(cnt,right-left+1)
                sum-=nums[left]
                left+=1
            right+=1
        return 0 if cnt==n+1 else cnt

