# -*- coding: utf-8 -*-
"""
主运行文件
"""
import subprocess




def run_main():
    """主函数"""
    cmd_all = (
        # "source env/bin/activate",
        "pytest tests/postman_demo/ --html=report.html --self-contained-html --alluredir allure-results --clean-alluredir --cache-clear",
        # "cp environment.properties allure-results",
        # "allure generate allure-results -c -o allure-report",
        # "allure open allure-report",
        "allure serve allure-results"  # 直接生成allure报告
    )
    for cmd in cmd_all:
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    run_main()
