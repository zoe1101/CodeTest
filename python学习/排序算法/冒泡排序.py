# -*- coding:utf-8 -*-
'''
冒泡排序重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端，故名。

步骤：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(1,n-i):
            if array[j-1]>array[j]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

#测试
data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
sorted_list = bubble_sort(data_test)
print(sorted_list)