'''
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

给你一个字符串 s，找到 s 中最长的回文子串。


示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

思路：动态规划


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return s
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        maxlen=1 # 最大回文子串长度
        begin=0 # 回文子串开始下标
        for j in range(n):
            dp[j][j]=True # 一个元素肯定是回文串
            for i in range(j):
                # 如果s[j] == s[i],且当串的长度小于等于2时，肯定是回文子串，如1，1，就是回文串。
                # 如果长度大于2时，则需要判断dp[i + 1][j - 1] 是不是回文。
                dp[i][j]=s[i]==s[j] and (j-i<2 or dp[i+1][j-1])
                if dp[i][j] and j-i+1>maxlen:
                    maxlen=j-i+1
                    begin=i
        return s[begin:begin+maxlen]



