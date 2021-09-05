'''
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

输入：ransomNote = "aa", magazine = "ab"
输出：false
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_map={}
        magazine_map={}
        for c in ransomNote:
            ransomNote_map[c]=ransomNote_map.get(c,0)+1
        for c in magazine:
            magazine_map[c] = magazine_map.get(c, 0) + 1
        for c in ransomNote:
            if c not in magazine_map or ransomNote_map[c]> magazine_map[c]:
                return False
        return True