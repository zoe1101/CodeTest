'''
给你一个非负整数 x ，计算并返回x的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。



示例 1：

输入：x = 4
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=0,x
        ans=-1
        while left<=right:
            mid=(left+right)>>1
            tmp=mid*mid
            if tmp<=x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans