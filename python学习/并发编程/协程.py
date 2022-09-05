import time

# 简化版 爬虫
'''
普通版本
'''
# def crawl_page(url):
#     print('crawl {}'.format(url))
#     sleep_time=int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))
#
# def main(urls):
#     for url in urls:
#         crawl_page(url)
#
# main(['url_1', 'url_2', 'url_3', 'url_4'])

'''
协程版本1
'''
# import asyncio
#
# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
#
#
# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     for task in tasks:
#         await task
#
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
#
#

'''
协程版本2
'''
# import asyncio
#
# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
#
#
# async def main(urls):
#     tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
#     await asyncio.gather(*tasks)
#
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))


'''
协程实现生产者-消费者模型
'''
import asyncio
import random


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)

async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()
    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))

    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)


asyncio.run(main())
