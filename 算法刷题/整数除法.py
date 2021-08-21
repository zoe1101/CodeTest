'''
给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。
注意：
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8以及truncate(-2.7335) = -2
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,2^31−1]。本题中，如果除法结果溢出，则返回 2^31− 1

示例 1：

输入：a = 15, b = 2
输出：7
解释：15/2 = truncate(7.5) = 7


思路：简化边界值：都转化为负数，因为负数的范围比正数大

'''




class Solution:
    def myDiv(self,a, b):
        '''
    此算法的思想是：如果b的二倍小于等于a，那么把b加倍，同时把答案计数（ans）也加倍
    当不满足b的二倍小于等于a这个条件时，a-b作为新的a，递归计算
    当a小于b时，a/b为0，递归终结，返回0；
    为处理int.MinValue，a和b都是预处理为负数，上述大小关系颠倒即可。
        :param a:
        :param b:
        :return:
        '''
        if a>b:return 0
        cur=b
        ans=-1 #返回值也是负数，因为结果可能是int.MinValue
        while a-cur<=cur:  ##本来是cur+cur>=a，改写一下，防止cur+cur溢出
            ans+=ans
            cur+=cur
        return ans+self.myDiv(a-cur,b)

    def divide(self, a: int, b: int) -> int:
        isNeg=False
        if (a>0)^(b>0):isNeg=True ##有且只有一个值是负数，最终结果是负数
        #由于int.MinValue的绝对值大于int.MaxValue，我们把两数都转换为负数.  方便判断溢出条件
        if a>0:a=-a
        if b>0:b=-b
        ans=self.myDiv(a,b)
        if isNeg:return ans
        if ans==pow(-2,31):return pow(2,31)-1  ##计算结果是int.MinValue，又要改变正负号，溢出了，根据提议返回int.MaxValue
        return -ans



