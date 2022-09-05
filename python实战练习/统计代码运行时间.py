def func():
    sum = 0
    for i in range(1000):
        for j in range(1000):
            sum = sum + i + j
    print("sum = ", sum)


'''
方法1:调用time.time()模块方法
'''
import time

start_time = time.time()
func()
end_time = time.time()
run_time = end_time - start_time
print("运行时间：", run_time, "秒")

'''
方法2:调用time.clock()模块方法
'''
import time

# python 3.8以后，time.clock()方法已经移除；从python 3.3开始就已经弃用了，替代的方法是time.perf_counter()
# start_time=time.clock()
start_time = time.perf_counter()
func()
end_time = time.perf_counter()
run_time = end_time - start_time
print("运行时间：", run_time, "秒")

'''
方法3:调用datetime模块方法
'''

from datetime import datetime

start_time = datetime.now()
func()
end_time = datetime.now()
run_time = (end_time - start_time).seconds
print("运行时间：", run_time, "秒")

'''
上面3种都可以记录程序运行的时间，但是如果严格区分的话，还是有点不同。 
方法1和方法3都包含了其他程序使用CPU的时间，广义上也是程序开始到程序结束的运行时间。
方法2算只计算了程序运行的CPU时间
'''
