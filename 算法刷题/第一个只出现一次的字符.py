'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"
s = ""
返回 " "

思路：
哈希表
遍历字符串 s ，使用哈希表统计 “各字符数量是否 > 1”。
再遍历字符串 s ，在哈希表中找到首个 “数量为 1 的字符”，并返回。
'''

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic={} #统计每个字符是否出现了多次
        for c in s:
            dic[c]=not c in dic  ##Python 代码中的 not c in dic 整体为一个布尔值； c in dic 为判断字典中是否含有键 c 。
        print(dic)
        for c in s:
            if dic[c]:
                return c
        return " "


if __name__ == '__main__':
    while True:
        s=input('请输入字符串：')
        print(Solution().firstUniqChar(s))