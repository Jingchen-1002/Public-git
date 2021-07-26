# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    read yaml文件
"""

import os
import yaml
from api_test.config.config import PATH_FILE


class YamlHelper:

    def read_yaml(self, filename):
        with open(os.path.join(PATH_FILE, filename), 'r', encoding="utf-8") as f:
            datas = yaml.load(f, Loader=yaml.FullLoader)
        return datas
