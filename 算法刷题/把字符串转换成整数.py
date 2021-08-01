'''
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

int的范围为 -(2^31)~(2^31)-1
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        s=s.strip()
        lens=len(s)
        if lens==0:
            return 0
        number, flag = 0, 1
        # 符号位的判断是否有正负号
        if s[0]=='-':
            flag=-1
            s=s[1:]
        elif s[0]=='+':
            flag=1
            s=s[1:]
        # 遍历除+，-以外的所有字符，如果遇到非数字，则直接返回0
        for c in s:
            if c>'0' and c<'9':
                number=number*10+int(c)
            else:
                return 0
        return flag*number