# -*- coding:utf-8 -*-
# @Author:chenjing
import os
import configparser

config_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config")
print(config_dir)
config = configparser.ConfigParser()
config.read(config_dir + "\env.ini", encoding="utf-8")
url = config.get("apidemo01", "URL")
print(url)