'''
我们可以设置一个类，用列表来存放栈中元素的信息，利用列表的append()和pop()方法可以实现队列的入队enqueue和出队dequeue的操作，
上面栈一个元素每次出去是列表的最后一个，直接用list.pop()出栈，而出队列每次是第一个，所以要用list.pop(0)出队列
'''
class Queue():
    def __init__(self):
     self.__list =[]
    def isEmpty(self):
     '''判断队列是否为空'''
     return self.__list==[]
    def push(self,data):
        '''入队 '''
        self.__list.append(data)
    def pop(self):
        '''出队'''
        if self.isEmpty():
            return False
        return self.__list.pop(0)
    def __len__(self):
        return len(self.__list)
    def __str__(self):
        if self.isEmpty():
            return ''
        return ' '.join([str(x) for x in self.__list])

if __name__ == '__main__':
    q=Queue()
    print(q.isEmpty())
    for i in range(5):
        q.push(i)
    print(q.__str__())
    print(q.pop())
    print(q.__len__())


