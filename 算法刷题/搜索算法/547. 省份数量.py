'''
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。



示例 1：
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-provinces
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
本题拥有 n 个节点，每个节点最多有 n 条边，表示和所有人都是朋友，最少可以有 1 条边，表示自己与自己相连
'''
from typing import List



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        count=0
        visited=[False]*n
        def dfs(i):
            visited[i]=True
            for j in range(n):
                if isConnected[i][j]==1 and visited[j]==False:
                    dfs(j)

        for i in range(n):
            if visited[i]==False:
                dfs(i)
                count+=1
        return count

