'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]


思路：分组异或
对于两个操作数的每一位，相同结果为 00，不同结果为 11。那么在计算过程中，成对出现的数字的所有位会两两抵消为 00，最终得到的结果就是那个出现了一次的数字。


先对所有数字进行一次异或，得到两个出现一次的数字的异或值。
在异或结果中找到任意为 1的位。
根据这一位对所有的数字进行分组。
在每个组内进行异或操作，得到两个数字。

'''
import functools
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        div=1
        while div&ret==0:   ##找出所有异或结果位为1的位
            div<<=1
        a,b=0,0
        ##将不同的两个数分到不同组
        for n in nums:
            if n & div:
                a^=n
            else:
                b^=n
        return [a,b]
