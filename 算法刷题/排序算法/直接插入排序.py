'''
每步将一个待排序的纪录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。

步骤：从第二个元素开始，与左边的元素进行比较，如果该元素小于左边的元素就将进行交换

'''

# -*- coding:utf-8 -*-
def insert_sort(array):
    n=len(array)
    for i in range(1,n):
        for j in range(i,0,-1):
            if array[j-1]>array[j]:
                array[j],array[j-1] = array[j-1],array[j]
    return array

if __name__ == '__main__':
    data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
    sorted_list = insert_sort(data_test)
    print(sorted_list)

