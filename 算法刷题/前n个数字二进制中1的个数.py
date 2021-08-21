'''
给定一个非负整数 n，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。

示例 1:
输入: n = 2
输出: [0,1,1]
解释:
0 --> 0
1 --> 1
2 --> 10

思路：
偶数可以除以2，1的个数一定和除以2后的数的1的个数相同
奇数显然等于它的上一个数加1，因为上一个一定是偶数，最后一位是0，加1得到下一个数
'''
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for i in range(n+1):
            if i&1==0: #偶数
                ans[i]=ans[i>>1]
            else:
                ans[i] = ans[i-1]+1
        return ans
