def heapSort(array):
    n=len(array)
    if n<2:
        return array
    #建立大根堆
    buildMaxHeap(array,n)
    for i in range(n-1,0,-1): #交换堆顶和当前末尾的节点，重置大顶堆
        array[0],array[i]=array[i],array[0]
        n-=1
        heapify(array,n,0)
    return array


def buildMaxHeap(array,n):
    '''
    建立大根堆
    '''
    #从最后一个非叶节点开始向前遍历，调整节点性质，使之成为大顶堆
    for i in range(n//2-1,-1,-1):
        heapify(array,n,i)

def heapify(array,n,i):
    '''调整堆结构'''
    left=2*i+1
    right=2*i+2
    largest=i # 默认当前节点（父节点）是最大值
    if left<n and array[left]>array[largest]: #如果有左节点，并且左节点的值更大，更新最大值的索引
        largest=left
    if right<n and array[right]>array[largest]:#如果有右节点，并且右节点的值更大，更新最大值的索引
        largest=right
    if largest!=i: # 如果最大值不是当前非叶子节点的值，那么就把当前节点和最大值的子节点值互换
        array[i],array[largest]=array[largest],array[i]
        heapify(array,n,largest) #因为互换之后，子节点的值变了，如果该子节点也有自己的子节点，仍需要再次调整。


data_test = [10, 23, 1, 53, 11, 54, 16, 21, 65, 32, 35, 31]
sorted_list = heapSort(data_test)
print(sorted_list)



