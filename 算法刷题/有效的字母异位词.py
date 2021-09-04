'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。

输入: s = "anagram", t = "nagaram"
输出: true

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)) or set(s)!=set(t):
            return False
        from collections import Counter
        sc=Counter(s)
        tc=Counter(t)
        return sc==tc

