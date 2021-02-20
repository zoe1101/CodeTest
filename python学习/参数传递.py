'''
参数传递机制具有值传递（int、float等值数据类型）和引用传递（以字典、列表等非值对象数据类型为代表）两种基本机制。
值传递，应用的参数不发生更改。（传了个副本进去）
引用传递，引用的参数发生更改（传的是真实的地址）

python中还允许包裹方式的参数传递(不定量传参)，这为不确定参数个数和参数类型的函数调用提供了基础：
知识点：
在函数调用时，*会以单个元素的形式解包一个元组，使其成为独立的参数。
在函数调用时，**会以键/值对的形式解包一个字典，使其成为独立的关键字参数。

在python中，当*和**符号出现在函数定义的参数中时，表示任意数目参数。*arg表示任意多个无名参数，类型为tuple;**kwargs表示关键字参数，为dict，使用时需将*arg放在**kwargs之前，否则会有“SyntaxError: non-keyword arg after keyword arg”的语法错误。
'''

def func(a,*args):
    print(args)

func(1,2,3,4)  ##虽然传入1,2,3,4，但是解包为（1），（2,3,4），其中a是1，args是剩下的。

def func2(**kwargs):
    print(kwargs)

func2(a=1,b=2,c=3)


def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
# 传入4个参数，自动将后两位  拼接到成字典
person('Adam', 45, gender='M', job='Engineer')


# *args 和 **kwargs混合
def h(a,*args,**kwargs):
    print(a,args,kwargs)

h(1,2,3,x=4,y=5)



