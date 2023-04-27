import time
from concurrent.futures import ThreadPoolExecutor
from robot.api import logger
# 创建线程池
executor = ThreadPoolExecutor(10) ##线程池大小为10
def test_func(num1,num2):
    logger.console(f"{num1}+{num2}")
    time.sleep(5)
    return num1+num2

# for i in range(30):
#   future =executor.submit(test_func,i,i+1)
#   print(future.result())


results =executor.map(test_func,[i for i in range(30)],[i for i in range(30)])
for r in results:
    print(r)
