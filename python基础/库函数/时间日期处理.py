from datetime import datetime, date, timedelta
import time
from dateutil.relativedelta import relativedelta


class TimeHelper:
    def get_current_time(self):
        return datetime.now()

    def get_current_date(self):
        return date.today()

    def get_specify_time(self, in_time, **kwargs):
        return in_time + relativedelta(**kwargs)

    def time2timestamp(self, in_time):
        return time.mktime(in_time)

    def timestamp2time(self, in_time, format):
        return time.strftime(format, in_time)

    def time2str(self, in_time, format):
        return datetime.strftime(format, in_time)

    def str2time(self, in_time, format):
        return datetime.strptime(in_time, format)


def time_test():
    print(time.time())  # 时间戳,float类型  1683860407.5388353
    print(time.strftime("%Y-%m-%d %X"))  # 格式化时间,string类型  2023-05-12 11:00:55
    tl = time.localtime()  # 本地时区的struct_time  time.struct_time(tm_year=2023, tm_mon=5, tm_mday=12, tm_hour=11, tm_min=1, tm_sec=10, tm_wday=4, tm_yday=132, tm_isdst=0)
    print(tl)
    print(tl.tm_year)  # 获取年
    print(time.gmtime())  # UTC时区的struct_time


def datetime_test():
    print(datetime.now())  # 2023-05-12 11:07:46.296911
    print(datetime.now().month)  #当前月份 5
    print(datetime.now()+timedelta(days=-300))  # 计算300天前的时期


if __name__ == '__main__':
    th = TimeHelper()
    print('当前时间：', th.get_current_time())
    print('当前日期：', th.get_current_date())
    print('一年前的明天：', th.get_specify_time(in_time=datetime.now(), years=-1, days=+1))
    print(th.str2time('20230310', '%Y%m%d'))
    print(th.time2str('%Y%m%d', datetime.now()))
    print(th.time2timestamp(time.localtime()))
    print(th.timestamp2time(time.localtime(), '%Y-%m-%d %H:%M:%S'))



    # print(time_test())
    # print(datetime_test())

    # print('当前时间：', time.strftime("%Y-%m-%d %H:%M:%S"))  ##当前时间  2021-06-01 19:44:37
    # print('当前时间：', datetime.now())  ##当前时间,具体到毫秒 2021-06-01 19:44:37.824778
    # # 时间加减
    # print('昨天：', date.today() + timedelta(days=-1))  # 昨天日期   datetime.date(2018, 7, 16)
    # print('昨天：', (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d"))  # 昨天日期  '2018-07-16'
    # print('一周后', (date.today() + timedelta(weeks=1)).strftime("%Y-%m-%d"))  # 一周后  '2018-07-16'
    # print('一个小时前：',
    #       (datetime.now() + timedelta(hours=-1)).strftime("%Y-%m-%d %H:%M:%S"))  # 一个小时前  '2018-07-16 19:44:37'
    #
    # print('两年前', (date.today() + relativedelta(years=-2)).strftime("%Y-%m-%d"))  # 两年前  '2018-07-16'
    #
    # # 时间格式转换
    # # 时间转字符串
    # print('时间转字符串：', time.strftime("%Y-%m-%d %H:%M:%S"))  ##当前时间  2021-06-01 19:44:37
    # # 字符串转时间
    # print('字符串转时间：', time.strptime('2021-06-01 19:44:37', "%Y-%m-%d %H:%M:%S"))  ##当前时间  2021-06-01 19:44:37
    # # 时间转时间戳
    # print('时间转时间戳：', time.mktime(time.strptime('2021-06-01 19:44:37', "%Y-%m-%d %H:%M:%S")))  ##当前时间  2021-06-01 19:44:37
    # # 时间戳转时间
    # print('时间戳转时间：', time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  ##当前时间  2021-06-01 19:44:37
