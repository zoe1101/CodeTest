'''
归并排序，就是把两个已经排列好的序列合并为一个序列。
'''


# -*- coding:utf-8 -*-
# 算法逻辑比较简单，以第一个list为基准，第二个向第一个插空


def merge(left, right):
    i,j=0,0
    res=[]
    while i<len(left) and j<len(right):  # 判断列表里面是否还有元素可以用
        # 哪边的元素小于另外一边的的元素就把哪边的元素加入进去，对应的索引加一
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    # 下面的这两个就是，如果有一个列表全部添加了，另外一个列表剩下的元素直接添加到res后面
    res += left[i:]
    res += right[j:]
    return res


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    mid = n // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


#测试
data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
sorted_list = merge_sort(data_test)
print(sorted_list)
