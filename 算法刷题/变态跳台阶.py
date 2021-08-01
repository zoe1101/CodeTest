'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：n=0时,f(n)=0；n=1时,f(n)=1；n=2时,f(n)=2；假设到了n级台阶，我们可以n-1级一步跳上来，也可以不经过n-1级跳上来，所以f(n)=2*f(n-1)。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number<1:
            return 0
        f=[0,1,2]
        for i in range(3,number+1):
            f.append(2*f[i-1])
        return f[number]

if __name__ == '__main__':
    while True:
        number = input('请输入n：')
        print(Solution().jumpFloorII(int(number)))