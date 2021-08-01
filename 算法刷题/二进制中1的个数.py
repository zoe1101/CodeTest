'''
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。

思路：
把这个数逐次 右移 然后和1 与,
就得到最低位的情况,其他位都为0,
如果最低位是0和1与 之后依旧 是0，如果是1，与之后还是1。
对于32位的整数 这样移动32次 就记录了这个数二进制中1的个数了
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count