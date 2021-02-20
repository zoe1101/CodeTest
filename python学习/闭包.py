'''
我们可以将闭包理解为一种特殊的函数，这种函数由两个函数的嵌套组成，且称之为外函数和内函数，外函数返回值是内函数的引用，此时就构成了闭包。
Python中，闭包的主要用途就是用于装饰器的实现

def 外层函数(参数):
    def 内层函数():
        print("内层函数执行", 参数)

    return 内层函数


内层函数的引用 = 外层函数("传入参数")
内层函数的引用()

外层函数中的参数，不一定要有，据情况而定，但是一般情况下都会有并在内函数中使用到
'''

def func(a, b):
    def line(x):
        return a * x - b

    return line


line = func(2, 3)
print(line(5))


#内函数中修改外函数的值
def func(a, b):
    def line(x):
        nonlocal a  #如果想要在内函数中修改外函数的值，需要使用 nonlocal 关键字声明变量
        a = 3
        return a * x - b

    return line


line = func(2, 3)
print(line(5))