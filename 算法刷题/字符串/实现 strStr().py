'''
实现strStr()函数。
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。

说明：
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/array-and-string/cm5e2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


思路：KMP算法
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)
        if (m==0):
            return 0
        j=0
        next=[0]*m
        for i in range(1,m):
            while j>0 and needle[i]!=needle[j]:
                j=next[j-1]
            if needle[i]==needle[j]:
                j+=1
            next[i]=j
        j=0
        for i in range(n):
            while j>0 and haystack[i]!=needle[j]:
                j=next[j-1]
            if haystack[i]==needle[j]:
                j+=1
            if j==m:
                return i-m+1
        return -1