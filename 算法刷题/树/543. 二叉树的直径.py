'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。



示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回3, 它的长度是路径 [4,2,1,3] 或者[5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0 #最大直径
        def helper(node):
            if not node:# 访问到空节点了，返回0
                return 0
            left=helper(node.left) # 左儿子为根的子树的深度
            right=helper(node.right) # 右儿子为根的子树的深度
            self.res=max(left+right,self.res)
            return max(left,right)+1 #深度

        helper(root)
        return self.res

