'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

思路：可以构造一个辅助栈来判断弹出序列是不是和压栈序列对应。首先遍历压栈序列的元素push到辅助栈，判断是不是弹出序列的首元素，如果是，则弹出序列pop首元素（指针后移），如果不是，则继续push，再接着判断；直到遍历完了压栈序列，如果辅助栈或者弹出序列为空，则返回True，否则返回False
'''

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack=[]
        for i in pushV:
            stack.append(i)
            while stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
        return not stack