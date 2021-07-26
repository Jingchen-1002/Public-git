# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    读取ini文件
"""

import configparser
from api_test.config.config import INI_PATH


def read_ini(section, option):
    config = configparser.ConfigParser()
    config.read(INI_PATH, encoding='utf-8')
    value = config.get(section, option)
    return value
