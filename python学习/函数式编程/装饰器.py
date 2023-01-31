import functools

# 无参装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now() # 等同于 now=logs(now)


# 带参数的装饰器
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today() # 等同于 today=logger('DEBUG')(today)



'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
'''
def log(func):
    def wrapper(*args, **kw):
        print('begin call')
        c = func(*args, **kw)
        print('end call')
        return c
    return wrapper

@log
def case():
    print('hello world')

case()
# 运行结果
# begin call
# hello world
# end call

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('begin call: %s %s' % (text,func.__name__))
            c = func(*args, **kw)
            print('end call: %s %s' % (text,func.__name__))
            return c
        return wrapper
    return decorator
@log('execute')
def case():
    print('hello world')

case()
# 运行结果
# begin call: execute case
# hello world
# end call: execute case
