'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

思路：双指针，滑动窗口


'''
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i,j=1,1 ##滑动窗口的左右边界
        sum=0 ##滑动窗口中数字的和
        res=[]
        while i<=(target//2):
            if sum<target:
                sum+=j
                j+=1  # 右边界向右移动
            elif sum>target:
                sum-=i
                i+=1 ## # 左边界向右移动
            else:
                res.append(range(i,j))
                # 左边界向右移动
                sum -= i
                i += 1
        return res



