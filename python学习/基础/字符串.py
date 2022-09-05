# 获取字符串长度或字节数

print(len('aa随便中文'))
print(len('aa随便中文'.encode())) #通过使用 encode() 方法，将字符串进行编码后再获取它的字节数。例如，采用 UTF-8 编码方式
print(len('aa随便中文'.encode('gbk'))) #获取采用 GBK 编码的字符串的长度
# 分割字符串
s='a s\n\nv'
print(s.split())  #sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。

# 合并字符串
print(','.join(s.split()))

# 统计字符串出现的次数
print('abcfvghtssvs'.count('s'))

# 检测字符串中是否包含某子串
print('abcfvghtssvs'.find('a')) #如果包含，则返回第一次出现该字符串的索引；反之，则返回 -1。
print('abcfvghtssvs'.index('a')) #当指定的字符串不存在时，index() 方法会抛出异常。

# 字符串对齐方法 （ljust()、rjust()和center()）
S = 'http://c.biancheng.net/python/'
addr = 'http://c.biancheng.net'
print(S.ljust(35))
print(addr.ljust(35))