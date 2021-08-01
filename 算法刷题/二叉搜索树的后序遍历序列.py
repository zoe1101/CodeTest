'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。

思路：递归判断。如果序列的长度小于2，那一定是后序遍历的结果。根据BST和后序遍历的性质，遍历结果的最后一个一定是根节点，那么序列中前面一部分小于根节点的数是左子树，后一部分是右子树，递归进行判断。
'''

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        return self.subVerifySquenceOfBST(sequence)
    def subVerifySquenceOfBST(self, sequence):
        if len(sequence) <= 2:
            return True
        flag = sequence[-1]
        index = 0
        while sequence[index] < flag:
               index += 1
        j = index
        while j < len(sequence)-1:
            if sequence[j] > flag:
                j += 1
            else:
                return False
        return self.subVerifySquenceOfBST(sequence[:index]) and self.subVerifySquenceOfBST(sequence[index:-1])