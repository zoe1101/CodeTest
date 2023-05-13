# 1.创建空字典
dic = {}
print(dic)
dic = dict()
print(dic)

# 2.创建多个元素的字典：
dic = dict(a=1,b=2) #注意：该方式键作为形参名使用不可以添加引号，必须符合变量规则
print(dic)
dic = dict([('a',1),('b',1)])
print(dic)
dic = dict(zip(('a','b'),(1,2)))
print(dic)

dic2=dic.fromkeys('a')
print('dic2',dic2)

# 删除信息
del dic['a'] # 删除键 'a'一个元素值
print(dic)
dic.clear()     # 清空字典
print(dic)
del dic         # 删除字典