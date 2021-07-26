# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    日志类
"""
import logging
import os
from ui_test_auto.config.config import LOG_PATH


class Log:
    def __init__(self):
        """创建一个日志器"""
        self.logger = logging.getLogger()
        """设置日志级别"""
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            """定义日志格式"""
            formatter = logging.Formatter(self.fmt)
            """创建一个输出到控制台的处理器"""
            sh = logging.StreamHandler()
            self.logger.addHandler(sh)
            """设置控制台的格式"""
            sh.setFormatter(formatter)
            """创建文件处理器，将日志输出到指定的文件目录"""
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
            self.logger.addHandler(fh)
            """设置日志格式"""
            fh.setFormatter(formatter)

    @property
    def log_path(self):
        """设置文件log输出路径"""
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        return os.path.join(LOG_PATH, 'test.log')

    @property
    def fmt(self):
        """设置日志格式"""
        return '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'


log1 = Log().logger
if __name__ == '__main__':
    log1.info('你好，HelloWorld')
