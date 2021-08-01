'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

思路：后序遍历 + 剪枝 （从底至顶）
对二叉树做后序遍历，从底至顶返回子树深度，若判定某子树不是平衡树则 “剪枝” ，直接向上返回。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root:
                return 0
            left=recur(root.left)  ##左子树时候平衡，不平衡表示为-1
            if left==-1:
                return -1
            right=recur(root.right)  ##右子树时候平衡
            if right == -1:
                return -1
            return max(left,right)+1 if abs(left-right)<2 else -1
        return recur(root)!=-1