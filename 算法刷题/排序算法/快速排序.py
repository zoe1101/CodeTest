'''
随意选择一个数字作为基准，比基准数字大的在右，比基准数字小的在左。
'''
import random


def quick_sort(array,start,end):
    if start>=end:
        return array
    pivot_idx = random.randint(start, end)  # 随机选择pivot基准元素
    array[start], array[pivot_idx] = array[pivot_idx], array[start]  # pivot放置到最左边
    pivot=array[start]
    left,right=start,end
    while left<right:
        while right>left and array[right]>pivot:
            right-=1
        while right>left and array[left]<=pivot:
            left+=1
        if left<right:
            array[left],array[right]=array[right],array[left]
    array[start],array[left]=array[left],array[start]
    quick_sort(array,start,left-1)
    quick_sort(array,left+1,end)
    return array

#测试
data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
sorted_list = quick_sort(data_test,0,len(data_test)-1)
print(sorted_list)



