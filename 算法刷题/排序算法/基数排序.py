
def radix_sort(array):
    i=0 # 记录当前正在排序的位
    maxn=max(array) # 最大值
    n=len(str(maxn)) # 记录最大值的位数

    while i<n:
        bucket_list=[[] for _ in range(10)] #初始化桶数组
        for a in array:
            bucket_list[a//(10**i)%10].append(a) # 找到位置放入桶数组
        index=0
        for a in bucket_list: # 放回原序列
            for b in a:
                array[index]=b
                index+=1
        i+=1
    return array


data_test =[334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
sorted_list = radix_sort(data_test)
print(sorted_list)