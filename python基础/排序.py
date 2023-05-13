'''
列表排序[]
字典排序{}
嵌套结构排序：[()],[{}],{[]}
https://blog.csdn.net/weixin_43507484/article/details/109058980?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-4-109058980-blog-123833939.235^v35^pc_relevant_increate_t0_download_v2_base&spm=1001.2101.3001.4242.3&utm_relevant_index=5
'''

# 列表排序
lis = [2, 5, 10, 4, 100, 12, 3]
lis.sort()  # 升序。该方法没有返回值，但是会对列表的对象进行排序。
print(lis)

lis = [2, 5, 10, 4, 100, 12, 3]
print(sorted(lis, reverse=True))  # 逆序，此方法不会改变原list数据, 返回重新排序的列表。
print(lis)

# 字典排序
dic = {'ac': 5, 'ab': 4, 'bc': 2, 'cc': 1, 'bb': 2}
list(dic.items()).sort(key=lambda x: x[1], reverse=False)  # 按照value正序排序
print(dic)
print(sorted(dic.items(), key=lambda x: x[0], reverse=True))  # 按照key逆序排序

# 嵌套排序
# [()],[[]]
lis = [(7, 7), (2, 3), (4, 1), (3, 2), (10, 5)]
print(sorted(lis, key=lambda x: x[1]))  # 按照第二个元素升序排序

# [{}]
lis = [{'letter': 'b'}, {'letter': 'c'}, {'letter': 'd'}, {'letter': 'a'}]
lis.sort(key=lambda x: x['letter'], reverse=True)  # 按照value逆序
print(lis)

# {{}}
dic = {'a': {'b': 'China'}, 'c': {'d': 'USA'}, 'b': {'c': 'Russia'}, 'd': {'a': 'Canada'}}
print(sorted(dic.items(), key=lambda x: list(x[1].items())[0][0], reverse=True))  # 根据值内的键降序排序

# {[]}
dic = {'a': [2, 3, 1], 'c': [2, 7, 3], 'b': [6, 0, 10], 'd': [3, 0, 7]}
print(sorted(dic.items(), key=lambda x: list(x[1])[1]))  # 根据值内第二个元素升序排序

# 多值排序
print(sorted(dic.items(), key=lambda x: (list(x[1])[1],list(x[1])[2])))  # 根据值内第二个元素/第三个元素升序排序
