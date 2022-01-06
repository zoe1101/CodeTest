'''
lambda 表达式是一行函数。
它们在其他语言中也被称为匿名函数。如果你不想在程序中对一个函数使用两次，你也许会想用 lambda 表达式，它们和普通的函数完全一样。

原型

    lambda 参数:操作(参数)
'''
add = lambda x, y: x + y
print(add(3, 5))
# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)

# 列表并行排序
list1=[2,4,6,3,7]
list2=[6,68,6,8,0]
data = zip(list1, list2)
data = sorted(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1,list2)
