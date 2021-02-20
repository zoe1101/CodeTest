'''
输入一个链表，反转链表后，输出新链表的表头。
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        curnode=pHead
        pre=None
        while curnode:
            temp=curnode.next
            curnode.next=pre
            pre=curnode
            curnode=temp
        return pre