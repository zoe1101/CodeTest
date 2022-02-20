'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
思路：F(1)=1,F(2)=2,   F(N)=F(N-2)+F(N-1)(N>=3)
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number<1:
            return 0
        f=[0,1,2]
        for i in range(3,number+1):
            f.append(f[i-2]+f[i-1])
        return f[number]

if __name__ == '__main__':
    while True:
        number=input('请输入n：')
        print(Solution().jumpFloor(int(number)))
