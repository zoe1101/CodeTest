'''
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

输入: n = 5, m = 3
输出:3


思路：约瑟夫环问题
对于「n,m 问题」，首轮删除环中第 m 个数字后，得到一个长度为n−1 的数字环。由于有可能 m>n ，因此删除的数字为 (m−1)%n ，删除后的数字环从下个数字（即 m%n ）开始，设 t=m%n ，可得数字环：
t,t+1,t+2,...,0,1,...,t−3,t−2
设「n−1,m 问题」某数字为 xx ，则可得递推关系：
x→(x+t)%n

换而言之，若已知「n−1,m 问题」的解 f(n−1) ，则可通过以上公式计算得到「n,m 问题」的解 f(n) ，即：
f(n)=(f(n−1)+t)%n=(f(n−1)+m%n)%n=(f(n−1)+m)%n
参见：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/jian-zhi-offer-62-yuan-quan-zhong-zui-ho-dcow/
'''

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        #f(n)=(f(n−1)+m)%n
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x