'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。



示例 1:

输入: s = "aba"
输出: true
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        isPalindrome = lambda x: x == x[::-1] ##判是否是回文字符串
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:#若不等，则判断删除左边元素或右边元素后，中间区域的字符串是否满足回文要求
                return isPalindrome(s[left+1:right+1]) or isPalindrome(s[left:right])
        return True
