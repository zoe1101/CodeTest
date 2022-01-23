'''
给你一个长度为n的整数数组，请你判断在 最多 改变1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的：对于数组中任意的i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-decreasing-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


思路：
当 nums[i] 破坏了数组的单调递增时，即 nums[i] < nums[i - 1] 时，为了让数组有序，我们发现一个规律（在上面三个例子中， nums[i]都为 2， nums[i -1]都为 4）：

当 i = 1，那么修改 num[i- 1]，不要动 nums[i]，因为nums[i]后面的元素是啥我们还不知道呢，少动它为妙。
当 i > 1时，我们应该优先考虑把 nums[i - 1]调小到 >= nums[i - 2] 并且 <= nums[i]。同样尽量不去修改 nums[i]，理由同上。
当 i > 1 且 nums[i] < nums[i - 2]时，我们无法调整 nums[i - 1]，我们只能调整 nums[i] 到 nums[i - 1]。

'''
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<=2:
            return True
        abnomal_count=0
        for i in range(1,n):
            if nums[i]<nums[i - 1]:
                abnomal_count+=1
                if i==1 or nums[i]>=nums[i-2]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
            if abnomal_count>1:
                return False
        return abnomal_count<=1