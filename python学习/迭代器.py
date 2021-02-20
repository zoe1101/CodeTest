'''
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''
import sys

list1=[1,2,3,4]
it=iter(list1)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素,一次输出一个
for x in it:
    print(x,end=' ')
print()
list1=[1,2,3,4]
it=iter(list1)
while True:
    try:
        print(next(it),end=' ')
    except StopIteration:
        sys.exit()


# 创建一个迭代器
class MyNumbers:
    '''把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。'''
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration



myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))