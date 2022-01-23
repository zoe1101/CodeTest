'''
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

示例 1：

输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        res=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i + 1]:
                res[i]=max(res[i],res[i+1]+1)
        return sum(res)
