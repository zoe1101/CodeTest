'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
'''

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if len(A)<2:
            return None
        B=[1]*len(A)
        cur=0
        while cur<len(A):
            for i in range(cur):
                B[cur]*=A[i]
            for j in range(cur+1,len(A)):
                B[cur] *= A[j]
            cur+=1
        return B

