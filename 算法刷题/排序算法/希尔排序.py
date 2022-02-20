'''
把记录按步长 gap 分组，对每组记录采用直接插入排序方法进行排序。【gap从N/减小到1】
'''

# -*- coding:utf-8 -*-
def shell_sort(array):
    n=len(array)
    gap= n // 2 # 初始步长
    while gap>0:
        for i in range(gap,n): # 按步长进行插入排序. i是需要比较的次数
            j=i # j 是需要控制的索引
            while j>=gap and array[j-gap]>array[j]:
                array[j - gap], array[j] = array[j], array[j - gap]
                j-= gap
        gap = gap // 2 # 得到新的步长
    return array

#测试
data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
sorted_list = shell_sort(data_test)
print(sorted_list)