'''
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

# -*- coding:utf-8 -*-
class Solution:
    def sumNums(self, n: int) -> int:
        ans=n
        temp=ans and self.sumNums(n-1)  ##python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
        ans+=temp
        return ans

if __name__ == '__main__':
    print(Solution().sumNums(50))
