'''
给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。



示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTreeHelper(inorder_start, inorder_end, preorder_start):
            if inorder_start>inorder_end:
                return None
            root_val=preorder[preorder_start]
            index=inorder_index[root_val]  # 根节点在中序遍历的索引位置
            leftlen= index - inorder_start - 1  # 根节点的左子树中的节点数目

            root=TreeNode(root_val) #建立根节点
            root.left=buildTreeHelper(inorder_start, index - 1, preorder_start + 1) # 递归地构造左子树，并连接到根节点
            root.right = buildTreeHelper(index + 1, inorder_end, preorder_start + 2 + leftlen) # 递归地构造右子树，并连接到根节点
            return root

        n=len(preorder)
        if n==0:
            return None
        # 构造哈希映射，帮助我们快速定位根节点
        inorder_index={e: i for i, e in enumerate(inorder)}
        return buildTreeHelper(0,n-1,0)

