# 无穷大与NaN
import math

print(math.isinf(float('inf')))
print(math.isnan(float('nan')))
# 四舍五入，近似值


print(round(32.345601, 3), round(32.345601, -1))

# 浮点数的一个普遍问题是它们并不能精确的表示十进制数。 并且，即使是最简单的数学运算也会产生小的误差。这些错误是由底层CPU和IEEE 754标准通过自己的浮点单位去执行算术时的特征。 由于Python的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的误差。
print((2.1 + 3.2) == 5.3)

from decimal import Decimal

# 使用 decimal 模块来处理浮点数的精确运算。decimal 模块主要用在涉及到金融的领域。
print(Decimal('2.1') + Decimal('3.2') == Decimal('5.3'))

# 数值格式化
print(format(3.23701, '0.2f'))  # 保留两位小数
print(format(3.23701, '<10.2f'))  # 左对齐

print(format(32567252.00245, ','))  # 千位符 ,分割

print(format(32567252.00245, '0.2E'))  # 指数表示

# 进制转换
print(hex(10))  # 16进制
print(bin(10))  # 2进制
print(int('1010', 2))
print(int('a', 16))
print(int('76', 8))

# 字节到大整数的打包与解包
# 将bytes解析为整数
print(int.from_bytes(b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004', 'big'))
print(int.from_bytes(b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004', 'little'))

# 将一个大整数转换为一个字节字符串
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
