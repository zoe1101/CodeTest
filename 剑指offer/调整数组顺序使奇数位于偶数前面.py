'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
遍历数组，从0到n，如果是奇数，i++，如果是偶数，将这个偶数插入到数组末尾，然后删除这个偶数，同时n--，确保不会出现全是偶数的情况下死循环或者遍历到了新插入的偶数上。
'''

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        n=len(array)
        i=0
        while i<n:
            if array[i]%2==1:
                i+=1
            else:
                array.append(array[i])
                del(array[i])
                n-=1
        return array

