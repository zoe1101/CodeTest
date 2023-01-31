import os
from loguru import logger

log_path = os.path.join(os.getcwd(), 'logs')
retention = '3 days'


class Log():
    def __init__(self, need_log=True):
        self.my_logger = logger

        # 判断是否需要写入日志
        if need_log is True:
            # 如果不存在这个logs文件夹，就自动创建一个
            if not os.path.exists(log_path):
                os.mkdir(log_path)
            # 每隔一段时间创建文件
            self.my_logger.add(os.path.join(log_path, 'runtime_{time}.logs'), encoding='utf-8', retention=retention)

    def info(self, content):
        self.my_logger.info(content)

    def debug(self, content):
        self.my_logger.debug(content)

    def error(self, content):
        self.my_logger.error(content)

    def critical(self, content):
        self.my_logger.critical(content)

    def warning(self, content):
        self.my_logger.warning(content)

    def success(self, content):
        self.my_logger.success(content)

    def trace(self, content):
        self.my_logger.trace(content)

    def traceback(self):
        import traceback
        self.my_logger.error(f'执行失败！！！失败信息：\n {traceback.format_exc()}')


if __name__ == '__main__':
    log = Log()
    log.error('出错啦！！')
