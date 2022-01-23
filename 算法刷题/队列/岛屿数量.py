'''
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

思路：广度优先遍历 或深度优先
https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-shu-liang-by-leetcode/

'''
import collections
from typing import List


class Solution:
    # 广度优先遍历
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        为了求出岛屿的数量，我们可以扫描整个二维网格。如果一个位置为 11，则将其加入队列，开始进行广度优先搜索。在广度优先搜索的过程中，每个搜索到的 11 都会被重新标记为 00。直到队列为空，搜索结束。
        最终岛屿的数量就是我们进行广度优先搜索的次数。
        :param grid:
        :return:
        '''
        nr=len(grid)
        if nr==0:
            return 0
        nc=len(grid[0])
        num_islands=0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=='1':
                    num_islands+=1
                    grid[r][c]='0'
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row,col=neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands
    # 深度优先遍历
    def numIslands1(self, grid: List[List[str]]) -> int:
        '''
        将二维网格看成一个无向图，竖直或水平相邻的 11 之间有边相连。

        为了求出岛屿的数量，我们可以扫描整个二维网格。如果一个位置为 11，则以其为起始节点开始进行深度优先搜索。在深度优先搜索的过程中，每个搜索到的 11 都会被重新标记为 00。
        最终岛屿的数量就是我们进行深度优先搜索的次数。
        :param grid:
        :return:
        '''
        nr=len(grid)
        if nr==0:
            return 0
        nc=len(grid[0])
        num_islands=0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=='1':
                    num_islands+=1
                    self.dfs(grid,r,c)
        return num_islands
    def dfs(self,grid,r,c):
        grid[r][c]=0
        nr,nc=len(grid),len(grid[0])
        for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0<=x<nr and 0<=y<nc and grid[x][y]=='1':
                self.dfs(grid,x,y)



if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))