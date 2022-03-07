'''
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-two-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:

    def missingTwo(self, nums: List[int]) -> List[int]:
        '''
         求和：
    找到缺失的一个数
    ->找到缺失的两个数
        :param nums:
        :return:
        '''
        n=len(nums)+2
        sums=sum(nums)
        sum_two=n*(n+1)//2-sums
        avg=sum_two//2
        sums=0
        for x in nums:
            if x<=avg: #计算平均数前半部分数的和
                sums+=x  #两个数不相同那么一个大于，一个小于
        one=avg*(avg+1)//2-sums #先找到小于avg的
        return [one,sum_two-one]


if __name__ == '__main__':
    import random
    n=100
    sample_nums=random.sample(range(1,n+1),n-2)
    print(sample_nums)
    print(Solution().missingTwo(sample_nums))