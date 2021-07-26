# -*- coding:utf-8 -*-
# @Author:chenjing
import unittest
import time

from api_test.util.client.httpcilent import HttpClient
from ddt import ddt, file_data
from api_test.config.config import PATH_FILE
import os
import jsonpath
import json


@ddt
class TestSwaggerAPI(unittest.TestCase):
    # SWAGGER_PATH = os.path.join(PATH_FILE, "swagger.yaml")
    SWAGGER_PATH = os.path.join(PATH_FILE, "swagger01.json")
    dic = {}

    @classmethod
    def setUpClass(cls) -> None:
        cls.httpclient = HttpClient()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.httpclient.close_session()

    @file_data(SWAGGER_PATH)
    def test_swagger(self, data):
        for item in data:
            print(item)
            print(type(item))
            # 字典转字符串
            item = json.dumps(item)
            item = item % TestSwaggerAPI.dic
            # 字符串转字典
            item = json.loads(item)
            ret = self.httpclient.send_request(url=item["url"],
                                               method=item["method"],
                                               params_type=item["params_type"],
                                               data=item["data"])
            print(ret.text)
            if item.get("assert_type"):
                self.assertEqual(item["assert_type"]["expect_code"],
                                 jsonpath.jsonpath(ret.json(), item["assert_type"]["get_code"])[0],
                                 msg="断言失败！")
            # add token to headers
            if item.get("get_token"):
                for item_info in item["get_token"]:
                    for key, value in item_info.items():
                        self.httpclient.session.headers.update({"{}".format(key):
                                                                    jsonpath.jsonpath(ret.json(), "{}".format(value))[
                                                                        0]})
            # add openid to dic
            if item.get("get_info"):
                for item_info in item["get_info"]:
                    for key, value in item_info.items():
                        TestSwaggerAPI.dic[key] = jsonpath.jsonpath(ret.json(), "{}".format(value))[0]
                        print(TestSwaggerAPI.dic)
            # time.sleep(2)


if __name__ == '__main__':
    unittest.main()
