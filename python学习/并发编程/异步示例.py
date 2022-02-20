import time
import asyncio
async def hello():
    asyncio.sleep(1)
    print(f"hello world:{time.time()}")

def run():
    for i in range(5):
        loop.run_until_complete(hello())  #把异步的任务丢给这个循环的run_until_complete()方法,事件循环会安排协同程序的执行。
loop=asyncio.get_event_loop()#主线程调用asyncio.get_event_loop()时会创建事件循环
if __name__ == '__main__':
    run()
