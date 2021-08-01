'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3]
输出：4


思路：
考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 33 的倍数。
因此，统计所有数字的各二进制位中 11 的出现次数，并对 33 求余，结果则为只出现一次的数字。


或者  先排序
先快排一下，然后很容易得到这个数组只有3种情况：
情况1: 数组是ABBBCCC...的类型，第一个A就是我们要的
情况2：数组是BBBACCC...的类型，中间的A就是我们要的
情况3:数组是BBB...CCCA的类型，最后的A就是我们要的

'''
from typing import List


class Solution:
    def singleNumber2(self, nums: List[int]) -> int:
        if not nums or len(nums)<=3:
            return 0
        nums.sort()
        if nums[0]!=nums[1]:  ##在头部
            return nums[0]
        elif nums[-1]!=nums[-2]:  ##在尾部
            return nums[-1]
        for i in range(1,len(nums)-1):  ##在中间
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
        return 0


    def singleNumber1(self, nums: List[int]) -> int:
        # 建立一个长度为 32 的数组 counts，记录所有数字的各二进制位的 1的出现次数。
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j]+=num&1
                num>>=1
        res, m = 0, 3
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[-i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

if __name__ == '__main__':
    nums=[2,34,25,9,80,100,14,58,44,62,79,24,3,62,30,3,29,85,25,85,86,83,11,25,97,42,12,67,79,2,39,34,35,54,83,34,54,74,24,86,5,2,86,42,29,79,5,14,73,74,12,5,29,44,42,73,62,1,3,54,100,85,11,23,1,97,84,46,97,11,24,14,84,12,46,73,9,58,44,83,39,74,67,67,35,39,30,84,80,35,100,46,9,30,1,80,58]
    print(Solution().singleNumber2(nums))