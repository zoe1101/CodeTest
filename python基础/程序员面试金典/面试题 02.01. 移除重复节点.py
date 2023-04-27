'''
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        occurred={head.val}
        pos=head
        #枚举前驱节点
        while pos.next:
            cur=pos.next # 当前待删除节点
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos=pos.next
            else:
                pos.next=cur.next
        return head