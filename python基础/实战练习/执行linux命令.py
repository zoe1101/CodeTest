import os

'''
os.system方法:
    在子终端运行系统命令，可以获取命令执行后的返回信息以及执行返回的状态
    执行后返回两行结果，第一行是结果， 第二行是执行状态信息
'''
print(os.system('date'))


'''
os.popen方法:
    不仅执行命令而且返回执行后的信息对象(常用于需要获取执行命令后的返回信息)，是通过一个管道文件将结果返回
'''
print(os.popen('date').read())

'''
commands模块:
    方法说明
        getoutput 获取执行命令后的返回信息
        getstatus 获取执行命令的状态值(执行命令成功返回数值0，否则返回非0)
        getstatusoutput 获取执行命令的状态值以及返回信息
'''
import commands
status, output = commands.getstatusoutput('date')
print(status)
print(output)

'''
注意1：在类unix的系统下使用此方法返回的返回值（status）与脚本或命令执行之后的返回值不等，这是因为调用了os.wait()的缘故，具体原因就得去了解下系统wait()的实现了。需要正确的返回值（status），只需要对返回值进行右移8位操作就可以了。
注意2：当执行命令的参数或者返回中包含了中文文字，那么建议使用subprocess。
'''

'''
subprocess模块:
    运用对线程的控制和监控，将返回的结果赋于一变量，便于程序的处理。有丰富的参数可以进行配置，可供我们自定义的选项多，灵活性高。之前我使用os.system的时候遇到文件描述符被子进程继承的问题，后来通过close_fds = False 这个参数来解决的。
'''
import subprocess
nowtime = subprocess.Popen('date', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(nowtime.stdout.read())