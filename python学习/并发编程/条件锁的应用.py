'''
需求：一个空列表，两个线程轮番往里面加值（一个加偶数，一个加奇数），最终让该列表中的值为 1 - 100 ，且是有序排列的。
'''

import threading

lst=[]

def even():
    """加偶数"""
    with condLock:
        for i in range(2, 101, 2):
            # 判断当前列表的长度处于2是否能处尽
            # 如果能处尽则代表需要添加奇数
            # 否则就添加偶数
            if len(lst) % 2 != 0:
                # 添偶数
                lst.append(i)      # 先添加值
                condLock.notify()  # 告诉另一个线程，你可以加奇数了，但是这里不会立即交出执行权
                condLock.wait()    # 交出执行权，并等待另一个线程通知加偶数
            else:
                # 添奇数
                condLock.wait()  # 交出执行权，等待另一个线程通知加偶数
                lst.append(i)
                condLock.notify()
        condLock.notify()
def odd():
    """加奇数"""
    with condLock:
        for i in range(1,101,2):
            if len(lst)%2==0:
                lst.append(i)
                condLock.notify()
                condLock.wait()
        condLock.notify()



if __name__ == '__main__':

    condLock=threading.Condition()
    addEvenTask =threading.Thread(target=even)
    addOddTask = threading.Thread(target=odd)
    addEvenTask.start()
    addOddTask.start()
    addEvenTask.join()
    addOddTask.join()

    print(lst)

