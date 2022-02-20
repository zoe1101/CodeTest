'''
假设你正在爬楼梯。需要 n阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：斐波那契数列题
F(1)=1
F(2)=2
F(N)=F(N-1)+F(N-2)

'''
class Solution:
    def climbStairs1(self, n: int) -> int: #对动态规划进行空间压缩
        if n<=2:
            return n
        pre2,pre1=1,2
        for i in range(2,n):
            cur=pre1+pre2
            pre2=pre1
            pre1=cur
        return cur
    def climbStairs(self, n: int) -> int: #典型动态规划
        if n<=2:
            return n
        dp=[1]*(n+1)
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]



