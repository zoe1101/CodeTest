'''
有2个任务线程来扮演李白和杜甫，如何让他们一人一句进行对答？文本如下：

杜甫：老李啊，来喝酒！

李白：老杜啊，不喝了我喝不下了！

杜甫：老李啊，再来一壶？

杜甫：...老李？

李白：呼呼呼...睡着了..
'''
import threading


def libai():
    event.wait()
    print("李白：老杜啊，不喝了我喝不下了！")
    event.set()
    event.clear()
    event.wait()
    print("李白：呼呼呼...睡着了..")

def dufu():
    print("杜甫：老李啊，来喝酒！")
    event.set()
    event.clear()
    event.wait()
    print("杜甫：老李啊，再来一壶？")
    print("杜甫：...老李？")
    event.set()


if __name__ == '__main__':

    event = threading.Event()

    t1 = threading.Thread(target=libai)
    t2 = threading.Thread(target=dufu)

    t1.start()
    t2.start()
    t1.join()
    t2.join()