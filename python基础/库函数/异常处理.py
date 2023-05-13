# coding : utf-8
'''
异常处理结构：

try:
    执行代码
except:
    发生异常执行的代码
else：
    没有异常执行的代码
finally:
    不管有没有异常都会执行的代码

'''


def demo1():
    try:
        uername = input("请你输入你的账号!")
        password = input("请你输入你的密码!")
        if uername == "admin" and password == "123456":
            print("登录成功")
        else:
            raise Exception('账号密码错误！')
        money = int(input("请输入取款金额"))
        if not int(money):
            raise Exception('输入的取款金额不满足数值要求')
    except Exception as err:
        print(err)
    else:
        print("请执行下一步")
    finally:
        return 'demo执行完毕！'

if __name__ == '__main__':
    demo1()
