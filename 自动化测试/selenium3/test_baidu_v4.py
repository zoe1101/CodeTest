import unittest
from HTMLTestRunner import HTMLTestRunner

# 定义测试用例的目录为当前目录下的 test_case 目录
test_dir = 'test_case'
suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # 生成 HTML 格式的报告
    fp = open('./test_report/result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="百度搜索测试报告",
                            description="运行环境： Windows 10, Chrome 浏览器"
                            )
    runner.run(suit)
    fp.close()
