'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"


思路：对str[0]按字符遍历，与其他字符串依次比较对应位置上的字符，并记录查找位置，如果找到不相等或者对应字符串的长度到了限制，就找到了。
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
