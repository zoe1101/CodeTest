'''
给你一个整数columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


输入：columnNumber = 1
输出："A"

输入：columnNumber = 701
输出："ZY"
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=list()
        while columnNumber>0:
            columnNumber-=1
            res.append(chr(columnNumber%26+ord('A')))  ##ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。
            columnNumber//=26
        return "".join(res[::-1])