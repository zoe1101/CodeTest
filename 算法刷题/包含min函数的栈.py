'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路：原栈+当前最小元素栈，两个栈中的元素数量始终保持一致，当新的元素小于“minstack”栈顶元素时，“minstack”像栈顶push新来的元素，
否则，“minstack”向栈顶加入原栈顶元素。
执行“pop”方法时，两个栈同时弹出各自的栈顶元素。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, node):
        self.stack.append(node)
        if not self.minstack or node<self.minstack[-1]:
            self.minstack.append(node)  #保存最小元素到栈顶
        else:
            self.minstack.append(self.minstack[-1])
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minstack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def min(self):
        if self.minstack:
            return self.minstack[-1]
        else:
            return  None
