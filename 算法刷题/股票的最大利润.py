'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价
思路：动态规划
profit=max(profit,prices[i]−min(cost,prices[i])

'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost,profit=float('+inf'),0
        for price in prices:
            cost=min(cost,price)
            profit=max(profit,price-cost)
        return profit