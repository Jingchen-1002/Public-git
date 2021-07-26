# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    读取配置
"""
import configparser
import os

from ui_test_auto.config.config import INI_PATH


HOST = 'HOST'


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError('配置文件不存在%s' % INI_PATH)
        self.config = configparser.RawConfigParser()
        self.config.read(INI_PATH, encoding='utf-8')

    """获取"""
    def _get(self, section, option):
        return self.config.get(section, option)

    @property
    def url(self):
        return self._get(HOST, HOST)


readconfig = ReadConfig()
if __name__ == '__main__':
    print(readconfig.url)
