'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
思路：从前向后记录‘ ’数目，从后向前替换‘ ’
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        if s=='':
            return s
        count=0
        slen=0
        for c in s:
            slen+=1
            if c==' ':
                count+=1
        s=list(s+' '*(2*count))
        for i in range(slen-1,-1,-1):
            if s[i]!=' ':
                s[i+2*count]=s[i]
            else:
                count-=1
                s[i+2*count]='%'
                s[i+2*count+1]='2'
                s[i+2*count+2]='0'
        return ''.join(s)

if __name__ == '__main__':
    while True:
        s = input('请输入字符串：')
        print(Solution().replaceSpace(s))