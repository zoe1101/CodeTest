'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

思路：动态规划
'''
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if len(grid)==0 or len(grid[0])==0:
            return 0
        m,n=len(grid),len(grid[0])
        for j in range(1,n):
            grid[0][j]+=grid[0][j-1]
        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=max(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

if __name__ == '__main__':
    grid=[
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
    print(Solution().maxValue(grid))