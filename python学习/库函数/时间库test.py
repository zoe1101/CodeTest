from datetime import datetime, date, timedelta
import time

print(time.strftime("%Y-%m-%d %H:%M:%S"))   ##当前时间  2021-06-01 19:44:37
print(datetime.now()) ##当前时间,具体到毫秒 2021-06-01 19:44:37.824778
yesterday = date.today() + timedelta(days = -1)    # 昨天日期   datetime.date(2018, 7, 16)
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")    # 昨天日期  '2018-07-16'