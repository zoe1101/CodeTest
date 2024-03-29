'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
    偷窃到的最高金额 = 1 + 3 = 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1) #dp[i] 表示抢劫到第 i 个房子时，可以抢劫的最大数量
        dp[1]=nums[0]
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
        return dp[n]

    # 对空间进行压缩。
    def rob1(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        pre2,pre1=0,nums[0]
        for i in range(1,n):
            cur=max(pre1,pre2+nums[i])
            pre2=pre1
            pre1=cur
        return cur