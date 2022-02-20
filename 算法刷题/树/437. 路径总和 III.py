'''
给定一个二叉树的根节点 root，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。


示例 1：

Input: sum = 8, tree =
10
/ \
5 -3
/ \ \
3 2 11
/ \ \
3 -2 1
Output: 3
在这个样例中，和为 8 的路径一共有三个： [[5,3],[5,2,1],[-3,11]]。

思路：递归每个节点时，需要分情况考虑：
（1）如果选取该节点加入路径，则之后必须继续加入连续节点，或停止加入节点
（2）如果不选取该节点加入路径，则对其左右节点进行重新进行考虑。
因此一个方便的方法是我们创建一个辅函数，专门用来计算连续加入节点的路径。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def pathSumStartWithRoot(root, targetSum):
            if not root:
                return 0
            count = 1 if root.val == targetSum else 0
            count += pathSumStartWithRoot(root.left, targetSum - root.val)
            count += pathSumStartWithRoot(root.right, targetSum - root.val)
            return count

        return 0 if not root else \
            pathSumStartWithRoot(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
