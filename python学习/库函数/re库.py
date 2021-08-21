import re

###compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
print(pattern.match('Hello World Wide Web').group(0))


# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.match( r'(.*) are (.*?) .*', 'Cats are smarter than dogs', re.M|re.I).group(1))
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search( r'(.*) are (.*?) .*', 'Cats are smarter than dogs', re.M|re.I).group(2))
#findall 在字符串中找到正则表达式所匹配的所有子串，
# 并返回一个列表，如果没有找到匹配的，则返回空列表。
str='runoob 123 google 456'
print(re.findall(r'\d+',str))
pattern = re.compile(r'\d+')   # 查找数字
print(pattern.findall('run88oob123google456', 0, 10))

# re.finditer:和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
it = pattern.finditer("12a32bc43jf3")
for match in it:
    print (match.group())


# 检索和替换
# re.sub用于替换字符串中的匹配项。
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
print(re.sub(r'#.*$', "", phone))
# 删除非数字(-)的字符串
print(re.sub(r'\D', "", phone))