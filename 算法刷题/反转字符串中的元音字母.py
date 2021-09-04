'''
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

输入：s = "hello"
输出："holle"


输入：s = "leetcode"
输出："leotcede"

思路：双指针
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
        s = list(s)
        left,right=0,len(s)-1
        while left<right:
            while(left<len(s)) and s[left] not in vowels:
                left+=1
            while(right>-1) and s[right] not in vowels:
                right-=1
            if left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)