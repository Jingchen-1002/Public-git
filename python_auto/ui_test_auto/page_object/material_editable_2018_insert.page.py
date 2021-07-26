# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    材质管理2018-编辑列表-新增页面
"""
from ui_test_auto.base_page.base_page import BasePage
from ui_test_auto.common.readconfig import readconfig


class InsertPage(BasePage):
    """网址"""
    url = readconfig.url + 'resources/material/dcb03d73-856c-4e8e-bd96-66816de636bf?type=material&mode=approval'
    """关键元素"""
    input_box = ('xpath', '//input[@name="resource"]')
    button_cloth = ('xpath', '//input[@ng-reflect-value="布料"]')
    add_package = ('xpath', '//span[text()="选择未打包文件"]/../input')
    add_pak = ('xpath', '//span[text()="选择 pak 文件"]/../input')
    tag_red = ('xpath', '//input[@ng-reflect-name="红色"]')
    tag_yellow = ('xpath', '//input[@ng-reflect-name="黄色"]')
    add_ini = ('xpath', '//span[text()="请选择 ini 文件"]/../input')
    add_su = ('xpath', '//span[text()="选择代理文件"]/../input')
    add_makefile = ('xpath', '//span[text()="选择制作文件"]/../input')
    save_button = ('xpath', '//button[text()="保存"]')

    """新增"""

    def insertResources(self, name, package, pak, ini, su, makefile):
        # 打开
        self.open(self.url)
        # 输入
        self.input(self.input_box, name)
        # 点击
        self.click(self.button_cloth)
        self.goto_wait(1)
        # 添加未打包文件
        self.input(self.add_package, package)
        self.goto_wait(1)
        # 添加pak文件
        self.input(self.add_pak, pak)
        self.goto_wait(1)
        # 点击红色标签
        self.click(self.tag_red)
        # 点击黄色标签
        self.click(self.tag_yellow)
        self.goto_wait(1)
        # ini信息
        self.input(self.add_ini, ini)
        self.goto_wait(1)
        # su代理
        self.input(self.add_su, su)
        self.goto_wait(1)
        # 添加制作文件
        self.input(self.add_makefile, makefile)
        self.goto_wait(1)
        # 点击保存
        self.click(self.save_button)


if __name__ == '__main__':
    pass
