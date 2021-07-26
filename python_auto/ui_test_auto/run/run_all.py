# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    运行主窗口
"""
import time
import unittest
from ui_test_auto.util.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 设置用例路径
    cases_path = '../test_case'
    # 添加套件
    discover = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern='bms*.py')
    # 设置报告路径
    report_dir = '../report/html/'

    # 报告文件
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    report_file = report_dir + "\\" + now + "_report.html"
    # 设置报告名称
    title = '11'
    # 报告描述
    description = '22'
    # 打开报告
    # The first way
    # fp = open(report_file, 'wb')
    # runner = HTMLTestRunner(stream=fp, title=title, description=description, verbosity=2)
    # runner.run(discover)
    # fp.close()
    # The second way
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title=title, description=description, verbosity=2)
        runner.run(discover)



"""
    3,确定测试用例存放路径
case_dir="./script"
4,确定测试报告存放路径
report_dir="./report"
5,命名测试报告的名,打开预定的测试报告,准备写入内容--->以当前时间命名测试报告
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=now+"report.html"#测试报告的名称
with open(os.path.join(report_dir,report_name),'wb',) as fp:
6,将要执行的测试用例,放入测试套件中
discover=unittest.defaultTestLoader.discover(case_dir)
7,执行测试用例,并生成HTL格式的测试报告
  runner=HTMLTestRunnerPlugins.HTMLTestRunner(title="eshop测试报告",description="登录功能",stream=fp,verbosity=2)
    runner.run(discover)
"""
