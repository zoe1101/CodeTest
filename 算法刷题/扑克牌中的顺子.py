'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

输入: [1,2,3,4,5]
输出: True

输入: [0,0,1,2,5]
输出: True

根据题意，此 5 张牌是顺子的 充分条件 如下：

除大小王外，所有牌 无重复 ；
设此 55 张牌中最大的牌为 max，最小的牌为 min （大小王除外），则需满足：max−min<5


思路：集合 Set + 遍历
遍历五张牌，遇到大小王（即 0）直接跳过。
判别重复： 利用 Set 实现遍历判重， Set 的查找方法的时间复杂度为 O(1) ；
获取最大 / 最小的牌： 借助辅助变量 ma 和 mi ，遍历统计即可。

'''
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        mi,ma=14,0
        for num in nums:
            if num==0:continue  # 跳过大小王
            ma=max(ma,num)  # 最大牌
            mi=min(mi,num)  # 最小牌
            if num in repeat:return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma-mi<5  # 最大牌 - 最小牌 < 5 则可构成顺子

