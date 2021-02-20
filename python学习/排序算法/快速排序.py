'''
随意选择一个数字作为基准，比基准数字大的在右，比基准数字小的在左。
'''

def quick_sort(array, low, high):
    if low>= high:
        return array
    left = low
    right = high
    k = array[left] ##基准值
    while left < right:
        while left < right and array[right] >= k:
            right = right-1
        array[left] = array[right]
        while left < right and array[left] <= k:
            left = left+1
        array[right] = array[left]
    array[left] = k
    quick_sort(array, low, left-1)
    quick_sort(array, right+1, high)
    return array

#测试
data_test=[10,23,1,53,11,54,16,21,65,32,35,31]
sorted_list = quick_sort(data_test,0,len(data_test)-1)
print(sorted_list)



