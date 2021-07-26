# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    bms-材质管理2018-更新列表页面
"""
from ui_test_auto.base_page.base_page import BasePage
from ui_test_auto.common.readconfig import readconfig


class MaterialUpdatePage(BasePage):
    """网址"""
    url = readconfig.url + 'resources/material/updates'
    """关键元素"""
    view_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div[1]/button[text()="查看"]')
    log_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div[1]/button[text()="日志"]')
    update_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div[1]/button[text()="更新"]')
    refresh_button = ('xpath', '//span[text()="REFRESH 刷新"]')
    """查看"""

    def viewButton(self):
        self.open(self.url)
        self.click(self.view_button)

    """日志"""

    def logButton(self):
        self.open(self.url)
        self.click(self.log_button)

    """更新"""

    def updateButton(self):
        self.open(self.url)
        self.click(self.update_button)

    """刷新"""

    def refreshButton(self):
        self.open(self.url)
        self.click(self.refresh_button)
