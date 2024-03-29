import time
import uuid
import funppy

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_random_request_id():
    return uuid.uuid4()



if __name__ == '__main__':
    funppy.register("get_httprunner_version", get_httprunner_version)
    funppy.register("sum_two", sum_two)
    funppy.serve()