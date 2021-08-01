'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5

思路:二分插入排序
二分插入排序，前面有多少个比它大的，当前数就有多少个逆序对，所有的加起来就是总的逆序对。

需要对原数组中的数取负数，这样就能直接获取到逆序对个数
'''
import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for v in nums:
            i = bisect.bisect_left(q,-v)  ##返回将会插入的位置，bisect_left(seq, x) x存在时返回x左侧的位置
            print(q,-v,i)
            res += i
            q[i:i] = [-v]  #将[n]元素插入到切切片索引的位置,s[i:i] = [x]类似于insert，s[len(s):len(s)] = [x]类似于append。
        return res

if __name__ == '__main__':
   nums= [7,5,6,4]
   print(Solution().reversePairs(nums))
