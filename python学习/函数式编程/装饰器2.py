from functools import wraps

# =================初级版本的装饰器=================
def mydec(func):
    def dec(*args):
        """
        your decorator code
        """
        return func(*args)

    return dec


# 下面是一个被装饰函数
def myfunc(*args):
    pass


# 最后，写下面的代码，相当于调用装饰器函数，传入被装饰函数
# 然后把内部具体实现装饰器功能的函数return并再次赋值给该被装饰器函数
myfunc = mydec(myfunc)
print(myfunc.__name__)


# =================装饰器的解决方案====================
def mydec(func):
    # 该行代码主要作用是将func的元信息，复制给dec函数
    @wraps(func)
    def dec(*args):
        """
        your decorator code
        """
        return func(*args)

    return dec


# 下面是一个被装饰函数，然后使用上面的装饰器进行装饰.该语句功能等同于  myfunc=mydec(myfunc)
@mydec
def myfunc(*args):
    pass

print(myfunc.__name__)



'''
@wraps(func)，可以理解为，这个本质也是一个装饰器，该装饰器的作用就是将func函数的元信息复制给被装饰的函数，元信息包括__name__，__doc__等信息，以下代码模拟了该装饰器的功能实现，主要是帮助大家深入理解装饰器的语法

'''
#以下定义自己的wraps装饰器，亲测有效，本质就是一个带参的装饰器，核心功能是复制函数元信息
def mywraps(fwrap):
    def out_dec(func):
        def in_dec(**args):
            return func(**args)
        meta_info=['__module__', '__name__', '__qualname__', '__doc__', '__annotations__']
        #以下代码，主要是逐个获取fwrap函数的以上元信息的值，并复制给dec函数，这样在最终使用该装饰器装饰函数的时候，看到的函数元信息不再是返回的dec的，而是fwrap的
        for meta in meta_info:
            setattr(in_dec,meta,getattr(fwrap,meta))
        #逐个获取fwrap函数的元信息，并复制到dec函数上
        return in_dec
    return out_dec