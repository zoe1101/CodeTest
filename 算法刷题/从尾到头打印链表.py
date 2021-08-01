'''
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

'''


# -*- coding:utf-8 -*-
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        curnode=listNode
        temp=[]
        while curnode!=None:
            temp.append(curnode.val)
            curnode=curnode.next
        res=[]
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
        return res