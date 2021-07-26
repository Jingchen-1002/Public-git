# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    登录页面
"""
import os
from ui_test_auto.base_page.base_page import BasePage
from selenium import webdriver
from ui_test_auto.common.readconfig import readconfig
import ui_test_auto.page_element.loginpage_ele
from ddt import ddt, file_data
from ui_test_auto.config.config import INI_PATH


class LoginPage(BasePage):
    """网址"""
    url = readconfig.url + 'auth/login'
    # url = os.path.join(INI_PATH, 'auth/login')

    """关键元素"""
    username = ('id', 'input-key')
    password = ('id', 'input-password')
    login_button = ('xpath', '//button[text()=" 登录 "]')

    """登录页面"""

    def loginPage(self, user, pwd):
        # 打开
        self.open(self.url)
        # 输入
        self.input(self.username, user)
        self.input(self.password, pwd)
        # 登录按钮
        self.click(self.login_button)
        self.goto_wait(1)
        self.click(self.login_button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'chenjing'
    pwd = 'cj123456'
    lp = LoginPage(driver)
    lp.loginPage(user, pwd)
