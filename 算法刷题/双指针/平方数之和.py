'''
给定一个非负整数c，你要判断是否存在两个整数 a 和 b，使得a2 + b2 = c 。



示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-square-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=math.floor(math.sqrt(c))
        while left<=right:
            sum=left*left+right*right
            if sum==c:
                return True
            elif sum<c:
                left+=1
            else:
                right-=1
        return False