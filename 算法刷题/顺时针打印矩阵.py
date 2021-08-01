'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.


思路：每次只取第一行数据，然后再把矩阵逆时针旋转90度，再打印第一行
'''
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while(matrix):
            res+=matrix.pop(0)
            matrix= list(zip(*matrix))[::-1]
        return res


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(list(zip(matrix)))
print(list(zip(*matrix))) ##加*可以实现矩阵转置
print(list(zip(*matrix))[::-1]) ##逆序读取转置后的矩阵
