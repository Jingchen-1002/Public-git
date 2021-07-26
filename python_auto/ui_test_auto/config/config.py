# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    配置文件ui
"""

import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.abspath(path='../ui_test_auto'))
# 日志目录
LOG_PATH = os.path.join(BASE_DIR, r'report\log')
# HTML报告目录
HTML_PATH = os.path.join(BASE_DIR, r'report\html')
# 截图目录
IMG_PATH = os.path.join(BASE_DIR, r'report\img')
# 读取ini文件
INI_PATH = os.path.join(BASE_DIR, 'config', 'url_path.ini')

if __name__ == '__main__':
    print(BASE_DIR)
    print(LOG_PATH)
    print(HTML_PATH)
    print(INI_PATH)
