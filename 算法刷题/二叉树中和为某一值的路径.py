'''
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

思路：按字典序打印是深度优先的意思
定义一个子函数，输入的是当前的根节点、当前的路径以及还需要满足的数值，同时在子函数中运用回溯的方法进行判断。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        self.res = []
        if not root:
            return []
        self.subPath(root,[],expectNumber)
        return self.res
    def subPath(self, root, path,number):
        if not root.left and not root.right:
            if number == root.val:
                self.res.append(path+[root.val])
        if root.left:
            self.subPath(root.left,path+[root.val],number-root.val)
        if root.right:
            self.subPath(root.right,path+[root.val],number-root.val)