import copy


class Information:
    """个人信息"""

    def __init__(self):
        self.name = None
        self.ager = None
        self.height = None

    def run(self):
        """
        自我介绍方法
        :return:
        """
        print("我叫{}： 年龄：{} 身高：{}".format(self.name, self.ager, self.height))


class Prototype:
    def __init__(self, obj):
        self.copy_object = obj()

    def clone(self, **attr):
        obj = copy.deepcopy(self.copy_object)
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    test = Prototype(Information)
    a = test.clone(name='张山', ager="30", height='170cm')
    a.run()
    b = test.clone(name='李飞', ager="20", height='190cm')
    b.run()