# -*- coding:utf-8 -*-
# @Author: chenjing
"""
    基类
"""
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from ui_test_auto.util.logger import log1
from ui_test_auto.config.chrome_option import Options
from ui_test_auto.config.config import IMG_PATH


class BasePage(Options):
    """基类"""

    # def browser(self, type_):
    #     """利用反射机制定义浏览器对象"""
    #     # try:
    #     #     driver = getattr(webdriver, type_)(options=Options().option_conf())
    #     # except Exception as e:
    #     #     print(e)
    #     #     driver = webdriver.Chrome(options=Options().option_conf())
    #     # return driver
    #     """定义浏览器对象"""
    #     try:
    #         if type_ == 'Chrome':
    #             return webdriver.Chrome(options=Options().option_conf())
    #         else:
    #             return getattr(webdriver, type_)()
    #     except Exception as e:
    #         log1.error('请选择正确的浏览器%s' % e)

    def __init__(self, driver):
        """定义driver"""
        self.driver = driver
        """最大化窗口"""
        self.driver.maximize_window()
        """隐式等待10s"""
        self.driver.implicitly_wait(10)

    def open(self, text):
        """
        打开网址验证
        :param text:
        :return:
        """
        try:
            """添加日志"""
            log1.info("打开网页%s" % text)
            """获取url"""
            self.driver.get(text)
        except Exception as e:
            print("打开%s超时异常，请检查网络" % e)

    def locator(self, loc):
        """
        元素定位器
        :return: 元素
        """
        try:
            return self.driver.find_element(*loc)
        except Exception as e:
            log1.error('元素定位失败 %s' % e)

    def click(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        try:
            log1.info('正在点击')
            self.locator(loc).click()
        except Exception as e:
            log1.error('点击失败 %s' % e)

    def input(self, loc, text):
        """
        输入操作
        :param loc:
        :param text:
        :return:
        """
        try:
            log1.info('正在定位及元素{}，输入的文本为{}'.format(loc, text))
            self.locator(loc).send_keys(text)
        except Exception as e:
            log1.error('输入失败！%s' % e)

    def explicit_wait(self, loc):
        """
        显式等待：until
        :param loc:
        :return:
        """
        try:
            log1.info('正在进行显示等待'.format(loc))
            WebDriverWait(self.driver, 10, 0.5).until(
                lambda el: self.locator(loc), message='元素未找到'
            )
        except Exception as e:
            log1.error('等待超时元素未找到 %s ' % e)

    def explicit_wait_not(self, loc):
        """
        显式等待: until_not
        :param loc:
        :return:
        """
        try:
            log1.info('正在进行显式等待'.format(loc))
            WebDriverWait(self.driver, 10, 0.5).until_not(
                lambda el: self.locator(loc), message='元素未消失'
            )
        except Exception as e:
            log1.error('等待超时元素依旧存在 %s' % e)

    def switch_windows(self, text):
        """句柄切换"""
        try:
            log1.info('正在切换句柄')
            all_hand = self.driver.window_handles
            self.driver.switch_to.window(all_hand[text])
        except Exception as e:
            log1.error('切换失败%s ' % e)

    def switch_windows_close(self, text):
        """
        句柄切换-关闭
        :param text:
        :return:
        """
        try:
            log1.info('正在切换句柄，并关闭上一个窗口')
            all_hand = self.driver.window_handles
            self.driver.close()
            self.driver.switch_to.window(all_hand[text])
        except Exception as e:
            log1.error('切换失败%s' % e)

    def switch_iframes(self, loc):
        """
        iframe切换
        :param loc:
        :return:
        """
        try:
            log1.info('正在定位iframe正在定位及元素{}，正在切换iframe'.format(loc))
            ele_iframe = self.locator(loc)
            self.driver.switch_to.frame(ele_iframe)
        except Exception as e:
            log1.error('切换失败 %s' % e)

    def goto_wait(self, s):
        """
        强制等待
        :param s:
        :return:
        """
        log1.info('正在等待...')
        time.sleep(s)

    def js_element(self, loc):
        """
        js定位
        :param loc:
        :return:
        """
        try:
            log1.info('正在进行js定位...')
            js = 'document.scrollingElement.scrollIntoView()'
            el = self.locator(loc)
            self.driver.execute_script(js, el)
        except Exception as e:
            log1.error('js定位失败！%s' % e)

    def assert_text(self, loc, except_text):
        """
        文本断言
        :param loc:
        :param except_text:
        :return: True or False
        """
        try:
            log1.info('正在进行断言')
            assert except_text == self.locator(loc).text, '断言失败'
            return True
        except:
            return False

    def action_move_element(self, loc):
        """
        元素悬停
        :param loc:
        :return:
        """
        try:
            log1.info('正在悬停元素')
            ActionChains(self.driver).move_to_element(self.locator(loc)).perform()
        except Exception as e:
            log1.error('元素悬停失败%s' % e)

    def save_screenshot(self):
        """
        截图
        :return:
        """
        try:
            log1.info('进行截图')
            if not os.path.exists(IMG_PATH):
                os.makedirs(IMG_PATH)
            self.driver.save_screenshot(IMG_PATH)

        except Exception as e:
            log1.error('截图失败%s' % e)

