'''
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：
输出坐标的顺序不重要
m 和 n 都小于150


示例：

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

在这个样例中，有括号的区域为满足条件的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pacific-atlantic-water-flow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m == 0:
            return []
        n = len(heights[0])

        res = []
        can_reach_p =[[False for _ in range(n)] for _ in range(m)]
        can_reach_a = [[False for _ in range(n)] for _ in range(m)]
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(can_reach, i, j):
            if can_reach[i][j]: return
            can_reach[i][j] = True
            if can_reach_p[i][j] and can_reach_a[i][j]:
                res.append([i, j])

            for a,b in direction:
                x = i + a
                y = j + b
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                    dfs(can_reach, x, y)

        for i in range(m):
            dfs(can_reach_p,i,0)
            dfs(can_reach_a,i,n-1)
        for i in range(n):
            dfs(can_reach_p,0,i)
            dfs(can_reach_a,m-1,i)
        return res

if __name__ == '__main__':
    h=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(h))