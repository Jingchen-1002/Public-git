# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    bms-材质管理2018-编辑列表页面
"""

from ui_test_auto.base_page.base_page import BasePage
from selenium import webdriver
from ui_test_auto.common.readconfig import readconfig
from ui_test_auto.config.chrome_option import Options


class MaterialEditablePage(BasePage):
    """页面网址"""
    url = readconfig.url + 'resources/material/editable'

    """关键元素"""
    insert_button = ('xpath', '//span[text()="NEW 新增"]')
    edit_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div/button[text()=" 编辑 "]')
    submit_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div/button[text()=" 提交 "]')
    del_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div/button[text()=" 删除 "]')
    log_button = ('xpath', '//tbody[@class="p-datatable-tbody"]/tr[1]/td[10]/div/button[text()=" 日志 "]')
    log_close = ('xpath', '//button[text()="关闭"]')

    """新增"""

    def insert(self):
        self.open(self.url)
        self.click(self.insert_button)
        return self.url

    """编辑"""

    def editButton(self):
        self.open(self.url)
        self.click(self.edit_button)

    """提交"""

    def submitButton(self):
        self.open(self.url)
        self.click(self.submit_button)

    """删除"""

    def delButton(self):
        self.open(self.url)
        self.click(self.del_button)

    """日志"""

    def logButtton(self):
        self.open(self.url)
        self.click(self.log_button)
        self.goto_wait(1)
        self.click(self.log_close)


if __name__ == '__main__':
    driver = webdriver.Chrome(options=Options().option_conf())
    ll = MaterialEditablePage(driver)
    print(ll.insert())
    # ll.editButton()
    # ll.submitButton()
    # ll.logButtton()
