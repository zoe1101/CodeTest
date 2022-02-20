def test_sort(array):
    n = len(array)
    if n < 2:
        return array
    mid = n // 2
    left = test_sort(array[:mid])
    right = test_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


# 测试
data_test = [10, 23, 1, 53, 11, 54, 16, 21, 65, 32, 35, 31]
sorted_list = test_sort(data_test)
print(sorted_list)
