'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

思路：根据题目的要求，两个数字m和n能拼接称数字mn和nm。如果mn<nm，也就是m应该拍在n的前面，我们定义此时m小于n；反之，如果nm<mn，我们定义n小于m。如果mn=nm,m等于n。
'''
from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=cmp_to_key(cmp))
        return ''.join(strs)
    

print(Solution().minNumber([3,32,321]))