
class people:
    """描述一个中国人类"""
    fuse="yellow"    #类属性1
    language = "chain"  # 类属性2

    # 构造方法---》名字特殊 __init__  调用特殊：实例化时调用
    # 什么时候会重构构造方法---》初始化数据
    def __init__(self,name,classname):
        print(f"实例化了一个对象，她的名称{name}，班级{classname}")
        self.name=name   #实例属性：实例对象自己私有。---》self.name   self.classname
        self.classname=classname

    #静态方法---》公共方法：类和对象公用
    @staticmethod
    def static_method():
        print("这是一个静态方法")

    # 类方法----》公共方法：类和对象公用
    @classmethod
    def class_method(cls):
        print(cls,type(cls))
        print("这是一个类方法")

    # 定义行为？ 说话 睡觉    ----》实例方法
    def speak(self):
        print(self,type(self))
        print("我说就是中国话")

    def __str__(self):
        return "欢迎来到码尚学院VIP-211期"

    def __getattribute__(self, item):
        if item=="name":
            return "名称"
        else:
            return object.__getattribute__(self,item)


    # def __del__(self):
    #     print("调用del方法，释放对象的内存地址")

# people.static_method()
DD=people("DD","211")
print(DD.name)
DD.static_method()
people.class_method()
DD.class_method()
