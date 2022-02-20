'''
给定一个大小为 n 的正方形国际象棋棋盘，求有多少种方式可以放置 n 个皇后并使得她们互不攻击，
即每一行、列、左斜、右斜最多只有一个皇后。

输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

类似于在矩阵中寻找字符串，本题也是通过修改状态矩阵来进行回溯。不同的是，我们需要
对每一行、列、左斜、右斜建立访问数组，来记录它们是否存在皇后。
本题有一个隐藏的条件，即满足条件的结果中每一行或列有且仅有一个皇后。这是因为我们
一共只有 n 行和 n 列。所以如果我们通过对每一行遍历来插入皇后，我们就不需要对行建立访问
数组了
'''
from typing import List




class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row==n:
                res.append([''.join(x) for x in board])
                return
            for i in range(n):
                print(i,n-row+i-1,row+i+1)
                if column[i] or ldiag[n-row+i-1] or rdiag[row+i]:
                        continue
                board[row][i]='Q'
                column[i]=ldiag[n-row+i-1]=rdiag[row+i]=True  #修改当前节点状态
                backtrack(row+1) #递归子节点
                # 回改当前节点状态
                board[row][i]='.'
                column[i]=ldiag[n-row+i-1]=rdiag[row+i]=False


        res=[]
        if n==0:
            return res
        board=[['.']*n for _ in range(n)]
        column=[False]*n
        ldiag=[False]*(2*n-1)
        rdiag=[False]*(2*n-1)
        backtrack(0)
        return res

if __name__ == '__main__':
    print(Solution().solveNQueens(4))
