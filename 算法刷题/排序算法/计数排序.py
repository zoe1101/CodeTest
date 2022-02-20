def countSort(array):
    n=len(array)
    if n<2:
        return array
    minn,maxn=array[0],array[0]
    for i in range(n):
        minn=min(array[i],minn)
        maxn=max(array[i],maxn)
    count_list=[0]*(maxn-minn+1) #记录某元素出现的次数
    for a in array:
        count_list[a-minn]+=1
    index=0
    for i in range(maxn-minn+1):
        while count_list[i]>0:
            array[index]=minn+i
            index+=1
            count_list[i]-=1
    return array

data_test = [10, 23, 1, 53, 11, 54, 16, 21, 65, 32, 35, 31]
sorted_list = countSort(data_test)
print(sorted_list)



