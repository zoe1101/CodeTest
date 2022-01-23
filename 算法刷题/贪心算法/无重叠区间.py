'''
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        if n<2:
            return 0
        intervals.sort(key=lambda x:x[1])
        ans=1
        index=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]>=index:
                ans+=1
                index=intervals[i][1]
        return n-ans

if __name__ == '__main__':
    Solution().eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ])