'''
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

'''

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        curnode=head
        res=[]
        while curnode!=None:
            res.append(curnode.val)
            curnode=curnode.next
        return res[::-1]