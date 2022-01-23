'''
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。



示例 1：

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


思路：
先对 dictionary 根据题意进行自定义排序：
    长度不同的字符串，按照字符串长度排倒序；
    长度相同的，则按照字典序排升序。
然后我们只需要对 dictionary 进行顺序查找，找到的第一个符合条件的字符串即是答案。

'''
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        n=len(s)
        for word in dictionary:
            m=len(word)
            i,j=0,0
            while i<n and j<m:
                if s[i]==word[j]:
                    j+=1
                i+=1
            if j==m:
                return word
        return ""

