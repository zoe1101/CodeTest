'''
输入一个链表，输出该链表中倒数第k个结点。
思路：快指针先往前走k步，注意判断边界，然后快慢一起走，当快指针为none的时候，慢指针走到了倒数第k个节点
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        slow,fast=head,head
        for i in range(k):
            if not fast:
                return None
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        return slow