'''
题目描述
判断一个二叉树是否对称。

输入输出样例
输入一个二叉树，输出一个布尔值，表示该树是否对称。
Input:
1
/ \
2 2
/ \ / \
3 4 4 3
Output: true


思路：
将判断两个子树是否相等或对称类型的题的解法叫做“四步法”：
（1）如果两个子树都为空指针，则它们相等或对称
（2）如果两个子树只有一个为空指针，则它们不相等或不对称
（3）如果两个子树根节点的值不相等，则它们不相等或不对称
（4）根据相等或对称要求，进行递归处理。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetric(leftNode,rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            if leftNode.val !=rightNode.val:
                return False
            return isSymmetric(leftNode.left,rightNode.right) and isSymmetric(leftNode.right,rightNode.left)
        return True if not root else isSymmetric(root.left,root.right)