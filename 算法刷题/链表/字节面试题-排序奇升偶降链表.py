'''
题目描述
给定一个奇数位升序，偶数位降序的链表，将其重新排序。

输入: 1->8->3->6->5->4->7->2->NULL
输出: 1->2->3->4->5->6->7->8->NULL

思路：
按奇偶位置拆分链表，得1->3->5->7->NULL和8->6->4->2->NULL
反转偶链表，得1->3->5->7->NULL和2->4->6->8->NULL
合并两个有序链表，得1->2->3->4->5->6->7->8->NULL
时间复杂度为O(N)，空间复杂度O(1)。
'''
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution():
    def sortOddEvenList(self,head):
        # 拆分成奇偶链表
        def partition(head:ListNode):
            evenHead=head.next
            even=evenHead
            odd=head
            while even and even.next:
                odd.next=even.next
                odd=odd.next
                even.next=odd.next
                even=even.next
            odd.next=None
            return head,evenHead

        # 翻转偶数链表
        def reverseList(head:ListNode):
            cur=head
            pre=None
            while cur:
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            return pre

        # 奇偶链表合并
        def merge(head1:ListNode,head2:ListNode):
            if not head1:
                return head2
            if not head2:
                return head1
            head=head1 if head1.val<head2.val else head2
            cur1=head1 if head==head1 else head2
            cur2=head2 if head==head1 else head1
            pre=None
            while cur1 and cur2:
                if cur1.val<=cur2.val:
                    pre=cur1
                    cur1=cur1.next
                else:
                    next=cur2.next
                    pre.next=cur2
                    cur2.next = cur1
                    pre=cur2
                    cur2=next
            pre.next=cur1 if cur1 else cur2
            return head

        if not head or not head.next:
            return head
        oddHead,evenHead=partition(head)
        evenHead=reverseList(evenHead)
        return merge(oddHead,evenHead)

if __name__ == '__main__':
    node1=ListNode(1)
    node2=ListNode(6)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(6)
    node6 = ListNode(1)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=node6

    head=Solution().sortOddEvenList(node1)
    while head:
        print(head.val)
        head=head.next





