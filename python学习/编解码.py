'''base64编码解码'''
import base64

a = base64.b64encode(b'binary\x00string')  # b'YmluYXJ5AHN0cmluZw=='
print(a)
b = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')  # b'binary\x00string'
print(b)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
a = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')  # b'abcd++//'
print(a)
b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')  # b'abcd--__'
print(b)
c = base64.urlsafe_b64decode('abcd--__')  # b'i\xb7\x1d\xfb\xef\xff'
print(c)
