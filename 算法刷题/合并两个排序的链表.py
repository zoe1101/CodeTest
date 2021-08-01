'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        curnode = ListNode(0)  ##当前节点
        pHead = curnode  ##定义新链表头结点
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                curnode.next = pHead1
                pHead1 = pHead1.next
            else:
                curnode.next = pHead2
                pHead2 = pHead2.next
            curnode = curnode.next
        if pHead1:
            curnode.next = pHead1
        if pHead2:
            curnode.next = pHead2
        return pHead.next

