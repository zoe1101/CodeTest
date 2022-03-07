'''
编写一个函数，检查输入的链表是否是回文的。

输入： 1->2
输出： false

思路:快慢指针
我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。
整个流程可以分为以下五个步骤：
找到前半部分链表的尾节点。
反转后半部分链表。
判断是否回文。
恢复链表。
返回结果。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        # 找到前半部分链表的尾节点
        slow=head
        fast=head
        while fast.next !=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next

        #反转后半部分链表
        behind_half_start=self.reverse_list(slow.next)

        # 判断是否回文
        res=True
        front=head
        behind=behind_half_start
        while res and behind!=None:
            if front.val!=behind.val:
                res=False
            front=front.next
            behind=behind.next

        # 还原链表并返回结果
        slow.next=self.reverse_list(behind_half_start)
        return res

    def reverse_list(self, head):
        pre = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
