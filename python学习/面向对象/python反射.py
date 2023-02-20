class TestObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        print("执行test方法")


def a():
    print("类的外部方法")


if __name__ == '__main__':
    """1.getattr 获取对象属性、对象方法"""
    xiaoyu = TestObject("小于", 20)
    # 获取对象的属性
    print(getattr(xiaoyu, "name"))
    # 获取对象的方法
    result = getattr(xiaoyu, "test")
    print(type(result))
    result()
    """2.hasattr 判断对象是否有对应的属性、方法"""
    if hasattr(xiaoyu, "address"):
        print(getattr(xiaoyu, "address"))
    if hasattr(xiaoyu, "name"):
        print(getattr(xiaoyu, "name"))
    """3.delattr 删除属性"""
    # delattr(xiaoyu,"name")
    """4.setattr 为对象设置内容"""
    # 修改属性的值
    setattr(xiaoyu, "name", "liuwei")
    print(getattr(xiaoyu, "name"))
    # 修改方法
    setattr(xiaoyu, "test11", a)
    getattr(xiaoyu, "test11")()
    # 相当于增加了test11方法
    xiaoyu.test11()
"""
去实现某个业务，定义类，类里面封装了很多方法，提供一个统一的入口能够调用各种方法
业务：登录   退出  注册  注销
"""


class Test:
    func_list = ["login", "loginOut", "register", "delete"]

    def login(self):
        print("这是登录")

    def loginOut(self):
        print("这是退出")

    def register(self):
        print("这是注册")

    def delete(self):
        print("这是注销")

    # 1.login    2.loginOut  3.register  4.delete
    def run(self, num):
        getattr(self, self.func_list[num - 1])()


num = int(input("请输入你的操作(1.login    2.loginOut  3.register  4.delete):"))
Test().run(num)