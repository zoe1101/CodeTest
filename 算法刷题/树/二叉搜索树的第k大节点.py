'''
给定一棵二叉搜索树，请找出其中第k大的节点。
示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
  2
输出: 4

思路：二叉搜索树的中序遍历倒序。中序遍历：左中右，倒序为：右中左
即求 “二叉搜索树第 k 大的节点” 可转化为求 “此树的中序遍历倒序的第 k 个节点”。

为求第 kk 个节点，需要实现以下 三项工作 ：
递归遍历时计数，统计当前节点的序号；
递归到第 kk 个节点时，应记录结果 resres ；
记录结果后，后续的遍历即失去意义，应提前终止（即返回）。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k==0:
                return
            self.k-=1
            if self.k==0:
                self.res = root.val
            dfs(root.left)
        self.k=k
        dfs(root)
        return self.res

