'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。

思路：堆排序，建立大根堆
初始化前 k 个数字进入最大堆，从 k+1 开始遍历后面的数
当新的数字比最大堆首的数字大的时候，我们弹出堆头，并把这个数字放入
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput)<k or k==0:
            return []
        self.buildHeap(tinput[:k],k) #先取前k个元素建立大根堆
        for i in range(k,len(tinput)):
            if tinput[i]<self.heap[0]: ##如果当前元素小于于堆顶元素
                self.heap[0]=tinput[i]
                self.perceDown(0,k)
        return sorted(self.heap)

    def buildHeap(self, tinput, k):
        self.heap=tinput
        for i in range(k//2,-1,-1):
            self.perceDown(i,k)

    def perceDown(self, i, k):
        temp=self.heap[i]
        while(2*i+1)<k:
            child=2*i+1
            if child<k-1 and self.heap[child]<self.heap[child+1]:
                child+=1
            if temp<self.heap[child]:
                self.heap[i]=self.heap[child]
                i=child
            else:
                break
            self.heap[i]=temp



