import schedule
import time


def job():
    print("her name is : ", name)


name = 'xiaona'
# 每隔十分钟执行一次任务
schedule.every(10).minutes.do(job, name)
# 每隔一小时执行一次任务
schedule.every().hour.do(job, name)
# 每天的10:30执行一次任务
schedule.every().day.at("10:30").do(job, name)
# 每隔5到10天执行一次任务
schedule.every(5).to(10).days.do(job, name)
# 每周一的这个时候执行一次任务
schedule.every().monday.do(job, name)
# 每周三13:15执行一次任务
schedule.every().wednesday.at("13:15").do(job, name)

while True:
    schedule.run_pending()  # run_pending：运行所有可以运行的任务
    time.sleep(1)
