def bucketSort(array):
    n=len(array)
    if n<2:
        return n
    #计算最大值与最小值
    minn=min(array)
    maxn=max(array)

    # 计算桶的数量
    bucket_num=(maxn-minn)//n+1
    #桶数组
    count_list=[[] for _ in range(bucket_num)]
    # 向桶数组填数
    for i in array:
        count_list[i//n].append(i)

    index=0
    for i in count_list:
        for j in sorted(i):
            array[index]=j
            index+=1
    return array
data_test = [10, 23, 1, 53, 11, 54, 16, 21, 65, 32, 35, 31]
sorted_list = bucketSort(data_test)
print(sorted_list)




