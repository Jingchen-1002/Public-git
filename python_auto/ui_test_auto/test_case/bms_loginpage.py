# -*- coding:utf-8 -*-
# @Author:chenjing

import unittest
from ddt import ddt, file_data
from selenium import webdriver
from ui_test_auto.config.chrome_option import Options
from ui_test_auto.page_object.login_page import LoginPage

"""
    Login process
"""


@ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=Options().option_conf())
        cls.login = LoginPage(cls.driver)

    @file_data('../data/loginpage.yaml')
    def test_01_login(self, user, pwd):
        self.login.loginPage(user, pwd)
        print(user)


if __name__ == '__main__':
    unittest.main()
