'''
在Python中，这种一边循环一边计算的机制，称为生成器：generator
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
最难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''

g = (x * x for x in range(10)) # 最简单的生成器

# 斐波拉契数列
#普通函数实现
def fib(n):
    i,a,b=0,1,1
    while i<n:
        print(b)
        a,b=b,a+b
        i+=1
    return 'done'

#使用生成器实现
def fib_g(n):
    i,a,b=0,1,1
    while i<n:
        yield b
        a,b=b,a+b
        i+=1
    return 'done'