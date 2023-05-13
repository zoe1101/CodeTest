class Animal(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print('父类方法:吃')

    def drink(self):
        print('父类方法:喝')

    def sleep(self):
        print('父类方法:睡')

    def speak(self):
        print('父类方法:说')

    def __private(self):
        print('这是一个私有方法')


class Cat(Animal):  # 继承
    def speak(self): # 多态，重写父类函数
        Animal.speak(self)  # 调用父类的方法，并且还需要进行扩展
        print('cat类方法:说')


class JiaFeiCat(Cat, Animal):  # 多继承
    def speak(self):  # 多态，重写父类函数
        print('我是JiaFeiCat：', self.name)


if __name__ == '__main__':
    animal1 = Animal('father', 100, 'male')
    print(animal1.name)
    cat = Cat('cat', 20, 'female')
    cat.speak()

    jiafeicat1 = JiaFeiCat('jiafeicat1', 2, 'male')
    jiafeicat1.speak()
