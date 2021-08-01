'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

思路：递归。把字符串分为两个部分： 字符串的第一个字符，第一个字符后面的所有字符。
1.求所有可能出现在第一个位置的字符，用索引遍历。
2.求第一个字符以后的所有字符的全排列。将后面的字符又分成第一个字符以及剩余字符。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        res = set()
        # 遍历字符串，固定第一个元素，第一个元素可以取a,b,c...，然后递归求解
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i] + ss[i+1:]): # 依次固定了元素，其他的全排列（递归求解）
                res.add(ss[i] + j) # 集合添加元素的方法add(),集合添加去重（若存在重复字符，排列后会存在相同，如baa,baa）
        return sorted(res)         # sorted()能对可迭代对象进行排序,结果返回一个新的list
