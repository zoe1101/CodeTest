'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''


# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return pHead
        newhead = RandomListNode(pHead.label)  # 新建一个链表的头结点
        newhead.random = pHead.random  # 令头结点的random等于原来头节点的random
        newhead.next = self.Clone(pHead.next)  # 令头结点的next等于原来头结点的next, 这里递归处理newhead.next
        return newhead
