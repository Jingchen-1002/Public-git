# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    Chrome配置
"""

from selenium import webdriver


class Options:

    def option_conf(self):
        """创建option对象：配置浏览器"""
        option = webdriver.ChromeOptions()
        """去掉白条提示"""
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        """窗体最大化"""
        option.add_argument('start-maximized')
        """添加配置去掉密码管理弹窗"""
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enabled'] = False
        option.add_experimental_option('prefs', prefs)
        """加载缓存模式"""
        option.add_argument(r'--user-data-dir=C:\Users\chenjing\AppData\Local\Google\Chrome\User Data')
        """无头模式"""
        option.add_argument('--headless')
        """隐身模式"""
        # option.add_argument('incognito')
        """去掉日志打印信息"""
        option.add_argument('log-level=3')

        return option
