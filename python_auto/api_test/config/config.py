# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    配置文件api目录
"""

import os

# 项目目录
BASE_DIR = os.path.join(os.path.dirname((os.path.dirname(__file__))))
# 日志目录
LOG_PATH = os.path.join(BASE_DIR, r'report\log')
# HTML报告目录
HTML_PATH = os.path.join(BASE_DIR, r'report\html')
# 用例路径  ps:如果进入套件中使用：可以单独设置目录
CASE_PATH = os.path.join(BASE_DIR, r'testcase')
# 用例 testxiaodiapi
XD_PATH = os.path.join(CASE_PATH, r'testxiaodiapi01')

# 驱动文件目录
PATH_FILE = os.path.join(BASE_DIR, r'data')

# ini文件目录
INI_PATH = os.path.join(BASE_DIR, r'env.ini')

if __name__ == '__main__':
    print(BASE_DIR)
    print(LOG_PATH)
    print(PATH_FILE)
    print(CASE_PATH)
    print(XD_PATH)
    print(HTML_PATH)
    print(INI_PATH)
