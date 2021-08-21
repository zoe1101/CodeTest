'''
给定一个字符串数组words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。


示例:
输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。

思路：
使用二进制的26位代表单词中字母是否出现
'''
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        flags =[0]*n
        ##1、使用二进制的26位记录每个单词中26个字母的出现情况，1为出现
        for i in range(n):
            for c in words[i]:
                flags[i]|=1<<(ord(c)-ord('a'))  ##flags[i]：26位，每位代表每个字母的出现情况
                print(flags)
        ##2、两个单词如果有相同字母，则与运算为1，没有为0
        res=0
        for i in range(n):
            for j in range(i+1,n):
                if flags[i] &flags[j]==0:
                    prod = len(words[i])* len(words[j])
                    res =max(res, prod)
        return res

if __name__ == '__main__':
    print(Solution().maxProduct(["abcw","baz","foo","bar","fxyz","abcdef"]))
