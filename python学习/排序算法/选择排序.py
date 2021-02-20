'''
从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
'''
def select_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(i,n):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
    return array
#测试
data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
sorted_list = select_sort(data_test)
print(sorted_list)