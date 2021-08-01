'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count=0
        numbers.sort()
        mid=numbers[len(numbers)//2]
        for i in numbers:
            if i==mid:
                count+=1
        if count>len(numbers)//2:
            return mid
        else:
            return 0