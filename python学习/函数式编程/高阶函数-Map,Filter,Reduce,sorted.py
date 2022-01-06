'''
Map 会将一个函数映射到一个输入列表的所有元素上。这是它的规范：

规范
map(function_to_apply, list_of_inputs)

'''
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))  # 实现将每个元素平方的操作
print(squared)

'''
filter 过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True。
 filter 类似于一个 for 循环，但它是一个内置函数，并且更快。
 
'''
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))

'''
当需要对一个列表进行一些计算并返回结果时，Reduce 是个非常有用的函数。举个例子，当你需要计算一个整数列表的乘积时。
'''
from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)

'''
sorted
'''
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))  # 按照绝对值排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

from operator import itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))  #按名字正序排序
print(sorted(students, key=lambda t: t[1])) #按成绩正序排序
print(sorted(students, key=itemgetter(1), reverse=True)) #按成绩倒序