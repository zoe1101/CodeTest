
##栈:先进后出
'''
我们可以设置一个类，用列表来存放栈中元素的信息，利用列表的append()和pop()方法可以实现栈的出栈pop和入栈push的操作，list.append(obj)意思是向列表添加一个对象obj,list.pop(index=-1)意思是删除指定位置的对象，默认是最后一个对象，也就是说list.pop(),是删除列表中下标最大的元素。
'''


class Stack():
    def __init__(self):
        self.__list = list()
    def isEmpty(self):
        return self.__list == []
    def push(self, data):
        self.__list.append(data)
    def pop(self):
        if self.isEmpty():
            return False
        return self.__list.pop()
    def __len__(self):
        return len(self.__list)
    def __str__(self):
        if self.isEmpty():
            return ''
        return ' '.join([str(x) for x in self.__list])

if __name__ == '__main__':
    s=Stack()
    print(s.isEmpty())
    for i in range(5):
        s.push(i)
    print(s.__str__())
    print(s.pop())
    print(s.__len__())

