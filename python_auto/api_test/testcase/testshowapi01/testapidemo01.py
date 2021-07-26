# -*- coding:utf-8 -*-
# @Author:chenjing
import unittest

from api_test.util.client.httpcilent import HttpClient
import os
import configparser
import jsonpath


class TestAPIDemo(unittest.TestCase):
    httpclient = None
    url = None
    token = None

    @classmethod
    def setUpClass(cls) -> None:
        TestAPIDemo.httpclient = HttpClient()
        config = configparser.ConfigParser()
        config_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config")
        print(config_dir)
        config.read(config_dir + "\env.ini", encoding="utf-8")
        # TestAPIDemo.url = config.get("apidemo01", "URL")
        TestAPIDemo.url = config.get("xiaodi", "URL")
        print(TestAPIDemo.url)

    # http://39.98.138.157:5000//api/login/
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # def test_Login(self):
    #     u'登录'
    #     path = "/api/login/"
    #     url = TestAPIDemo.url + path
    #     method = "post"
    #     data = {"username": "admin", "password": "123456"}
    #     ret = self.httpclient(method=method, url=url, params_type="json", json=data)
    #     print(ret)

    def test_all_category(self):
        u'分类列表'
        path = "/pub/api/v1/web/all_category"
        url = TestAPIDemo.url + path
        method = "get"
        ret = TestAPIDemo.httpclient.send_request(method=method, url=url, params_type="json")
        print(ret)
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..code")[0], 0, msg="业务状态错误!")

    def test_index_card(self):
        u'视频卡片'
        path = "/pub/api/v1/web/index_card"
        url = TestAPIDemo.url + path
        method = "get"
        ret = TestAPIDemo.httpclient(method=method, url=url, params_type="json")
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..code")[0], 0, msg="业务错误!")

    def test_01_web_login(self):
        u'登录'
        path = "/pub/api/v1/web/web_login"
        url = TestAPIDemo.url + path
        method = "post"
        data = {"phone": "15148189529", "pwd": "cj580231."}
        ret = TestAPIDemo.httpclient(method=method, url=url, params_type="form", data=data)
        print(ret.text)
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..code")[0], 0, msg="业务错误!")
        TestAPIDemo.token = jsonpath.jsonpath(ret.json(), "$..token")[0]
        print(TestAPIDemo.token)

    def test_user_info(self):
        u'个人信息'
        path = "/pub/api/v1/web/user_info"
        url = TestAPIDemo.url + path
        method = "get"
        headers = {"token": TestAPIDemo.token}
        ret = TestAPIDemo.httpclient(method=method, url=url, params_type="json", headers=headers)
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..code")[0], 0, msg="业务状态错误")
        self.assertTrue(len(jsonpath.jsonpath(ret.json(), "$..name")[0]) > 0, msg="名字字段为空！错误")

    def test_find_order(self):
        u'查询订单'
        path = "/user/api/v1/order/find_orders"
        url = TestAPIDemo.url + path
        method = "get"
        headers = {"token": TestAPIDemo.token}
        ret = TestAPIDemo.httpclient.send_request(method=method, url=url, params_type="json", headers=headers)
        print(ret.text)
        self.assertEqual(jsonpath.jsonpath(ret.json(), "$..code")[0], 0, msg="业务状态错误!")


if __name__ == '__main__':
    unittest.main()
