'''
Python 这种由多态衍生出的更灵活的编程机制，又称为“鸭子模型”或“鸭子类型”
参考： http://c.biancheng.net/view/5833.html
'''
class WhoSay:
    def say(self, who):
        who.say()


class CLanguage:
    def say(self):
        print("调用的是 Clanguage 类的say方法")


class CPython(CLanguage):
    def say(self):
        print("调用的是 CPython 类的say方法")


class CLinux(CLanguage):
    def say(self):
        print("调用的是 CLinux 类的say方法")


if __name__ == '__main__':
    '''
    通过给 WhoSay 类中的 say() 函数添加一个 who 参数，其内部利用传入的 who 调用 say() 方法。这意味着，当调用 WhoSay 类中的 say() 方法时，我们传给 who 参数的是哪个类的实例对象，它就会调用那个类中的 say() 方法。
    '''
    a = WhoSay()
    # 调用 CLanguage 类的 say() 方法
    a.say(CLanguage())
    # 调用 CPython 类的 say() 方法
    a.say(CPython())
    # 调用 CLinux 类的 say() 方法
    a.say(CLinux())
