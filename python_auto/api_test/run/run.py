# -*- coding:utf-8 -*-
# @Author:chenjing
import os
import unittest
import time
from datetime import datetime

from api_test.util.HTMLTestRunner import HTMLTestRunner
from api_test.config.config import HTML_PATH, XD_PATH

if __name__ == '__main__':
    """运行"""
    case_path = XD_PATH
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="test*.py")
    # 设置报告路径
    report_dir = HTML_PATH
    # l = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    # print("l={}".format(l))
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    report_file = report_dir + "\\" + now + "_report.html"

    title = "11"
    description = "22"
    # 判断文件是否存在
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    with open(report_file, "wb") as f:
        runner = HTMLTestRunner(stream=f, title=title, description=description, verbosity=2)
        runner.run(discover)
