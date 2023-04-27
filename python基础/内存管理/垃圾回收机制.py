import gc
import time


class A():
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' % str(hex(id(self))))


def f3():
    '''循环引用'''
    while True:
        c1 = A()
        c2 = A()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
        # 增加垃圾回收机制
        print(gc.garbage)
        print(gc.collect())
        print(gc.garbage)
        time.sleep(10)


if __name__ == '__main__':
    f3()
