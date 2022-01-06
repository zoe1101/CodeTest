'''
列表（list）推导式：variable = [out_exp for out_exp in input_list if out_exp == x]
字典（dict）推导式
集合（set）推导式
'''

# 列表推导式
print( [i for i in range(30) if i % 3 == 0])

# 字典推导式
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
print({v: k for k, v in mcase.items()})

# 集合推导式
print({x**2 for x in [1, 1, 2]})