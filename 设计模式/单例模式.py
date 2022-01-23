class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(Singleton,cls).__new__(cls)
        return cls.instance



# 懒汉式单例
class LazySingleton:
    __instance=None
    def __init__(self):
        if not LazySingleton.__instance:
            print('__init__ method called ...')
        else:
            print('instance already created:',self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance=LazySingleton()
        return cls.__instance



# Monostate（单态）模式。     Monostate 模式即类的所有实例对象共享相同的状态。
class Borg:
    __shared_state = {"1":"2"}
    def __init__(self):
        self.x=1
        self.__dict__ = self.__shared_state

# 通过修改 __new__ 方法来实现 Borg 模式：
class Borg1:
    __shared_state = {}
    def __new__(cls, name):
        obj = super().__new__(cls)
        obj.__dict__ = cls.__shared_state
        return obj

    def __init__(self, name):
        self.name = name

# 通过元类实现单例模式
class MetaSingleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            self.__instance = super().__call__(*args, **kwargs)
        return self.__instance


class Logger(metaclass=MetaSingleton):
    pass




if __name__ == '__main__':
    s = Singleton()
    print('object created', s)
    s1 = Singleton()
    print('object created', s1)

    print('====================================')

    s=LazySingleton()
    print('object created', LazySingleton.getInstance())  #LazySingleton.getInstance() 与 s.getInstance() 等价
    s1 = LazySingleton()
    print('object created', s1)
    print('====================================')
    b = Borg()
    b1 = Borg()

    print(b is b1)  # => False
    b.x = 4
    print(b.x)  # => 4
    print(b1.x)  # => 4
    print(b.__dict__)
    print(b1.__dict__)
    b1.x = 6
    print(b1.x)  # => 6
    print(b.x)  # => 6

    print('====================================')
    b1 = Borg1('Borg1')
    print(b1.name)  # => Borg1
    b2 = Borg1('Borg2')
    print(b2.name)  # => Borg2
    print(b1.name)  # => Borg2
    b1.name = 'Borg'
    print(b1.name)  # => Borg
    print(b2.name)  # => Borg
    print(b1 is b2)  # => False

    print('====================================')
    logger1 = Logger()
    logger2 = Logger()
    print(logger1, logger2)
    # => <__main__.Logger object at 0x7fac8af577c0> <__main__.Logger object at
    # 0x7fac8af577c0>
    print(logger1 is logger2)  # => True