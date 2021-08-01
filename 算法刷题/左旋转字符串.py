'''
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

'''


class Solution:
    #字符串切片
    def reverseLeftWords1(self, s: str, n: int) -> str:
        if not s or n>=len(s):
            return s
        return s[n:]+s[:n]

    ##列表遍历拼接
    def reverseLeftWords2(self, s: str, n: int) -> str:
        if not s or n>=len(s):
            return s
        res=[]
        for i in range(n,len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])
        return ''.join(res)