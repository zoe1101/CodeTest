'''
给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，
输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表
'''
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]
'''
# expected outout:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
 {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
 {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
'''
res = []
for i in range(len(values)):
    res.append({k: values[i][j] for j, k in enumerate(attributes)})

# 一行实现
res = [{k: values[i][j] for j, k in enumerate(attributes)} for i in range(len(values))]
res=[dict(zip(attributes, value)) for value in values]
print(res)
