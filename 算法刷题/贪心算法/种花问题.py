'''
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

 

示例 1：

输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev=-1 #表示上一朵已经种植的花的下标位置，初始时 \textit{prev}=-1prev=−1，表示尚未遇到任何已经种植的花。
        m=len(flowerbed)
        count=0
        for i in range(m):
            if flowerbed[i]==1:
                if prev<0:
                    count+=i//2
                else:
                    count+=(i-prev-2)//2
                if count>=n:
                    return True
                prev=i
        if prev<0: # 全是0时
            count+=(m-prev)//2
        else: ##结尾处
            count+=(m-prev-1)//2
        return count>=n