'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        ans=n
        temp=ans and self.Sum_Solution(n-1)  ##python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
        ans+=temp
        return ans

if __name__ == '__main__':
    print(Solution().Sum_Solution(50))
