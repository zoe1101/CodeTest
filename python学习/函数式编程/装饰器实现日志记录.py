from functools import wraps
import datetime

#定义一个可以记录函数调用时间、传入参数的装饰器
def dec(log_file):
    #接受log_file参数，供具体实现装饰器功能的函数使用
    def dec_print_info(func):
        @wraps(func)
        def print_info(a,b):
            # 该函数，因为本身没有定义log_file变量，python此时会逐层往上找寻，找到了最外层传入的log_file变量，然后使用
            with open(log_file,'a+',encoding='utf-8') as f:
                hour=datetime.datetime.now().hour
                minute = datetime.datetime.now().minute
                second = datetime.datetime.now().second
                f.write(f'调用时间：{hour}点{minute}分{second}秒，传入的参数为：{a}和{b}\n')
            return func(a,b)
        return print_info
    return dec_print_info

#加装饰器时，传入日志文件地址
@dec('log.txt')
def myfunc(a,b):
    return a+b

myfunc(11,22)