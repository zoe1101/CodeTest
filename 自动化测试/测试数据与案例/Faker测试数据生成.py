import os

from faker import Faker

'''
具体的支持的语言列表可以见：https://faker.readthedocs.io/en/master/locales.html
常见的语言：
简体中文：zh_CN
繁体中文：zh_TW
美国英文：en_US
英国英文：en_GB
德文：de_DE
日文：ja_JP
韩文：ko_KR
法文：fr_FR
'''
fake = Faker('zh_CN') #初始化，使用中文库。英文：en_US。

# 还支持多个区域设置。
# fake = Faker(['it_IT', 'en_US', 'ja_JP'])


print('随机生成姓名：', fake.name())  #Each call to method fake.name() yields a different (random) result.

print('随机生成地址：', fake.address())

print('随机生成身份证号码：', fake.ssn())


print('随机生成文本段：', fake.text())

print('随机生成日期：', fake.date())

print('生成随机数：', fake.random_number())


from faker.providers import internet
fake.add_provider(internet)
print('随机生成IPV4地址：', fake.ipv4_private())


# 命令行调用
os.system('faker -l zh_CN address')

'''
更多示例参考：
http://www.taodudu.cc/news/show-4418826.html?action=onClick
'''


from faker.providers import BaseProvider

# 创建自定义的Provider生成数据
class MyProvider(BaseProvider):
    def foo(self) -> str:
        return 'bar'

fake.add_provider(MyProvider)
print(fake.foo())

