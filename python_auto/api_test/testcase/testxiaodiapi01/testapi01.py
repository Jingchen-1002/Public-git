# -*- coding:utf-8 -*-
# @Author:chenjing
import json

from api_test.util.client.httpcilent import HttpClient
import os
import jsonpath
from ddt import ddt, file_data
import unittest
from api_test.config.config import PATH_FILE


@ddt
class TestXDAPI(unittest.TestCase):
    arg_dic = {}
    # os.path.join(path, "data01.yaml")
    # path01 = os.path.join(path, "data01.yaml")
    # path02 = os.path.join(path, "data02.yaml")
    # path03 = os.path.join(path, "data03.yaml")
    PATH_JSON = os.path.join(PATH_FILE, "data.json")
    PATH_JSON01 = os.path.join(PATH_JSON, "data01.json")

    # print(path01)
    @classmethod
    def setUpClass(cls) -> None:
        cls.httpclient = HttpClient()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.httpclient.close_session()

    @file_data(PATH_JSON)
    # @unittest.skip
    def testcase01(self, data):
        for item in data:
            # print(item)
            ret = self.httpclient.send_request(method=item["method"],
                                               url=item["url"],
                                               params_type=item["params_type"],
                                               data=item["data"])
            print(ret.text)
            self.assertEqual(item["assert_info"]["except_code"],
                             jsonpath.jsonpath(ret.json(), item["assert_info"]["get_node"])[0],
                             msg="返回code='{}'错误!".format(
                                 jsonpath.jsonpath(ret.json(), item["assert_info"]["get_node"])[0]))
            # 判断参数----添加到headers中
            if item.get("get_info"):
                for item_info in item["get_info"]:
                    for key, value in item_info.items():
                        self.httpclient.session.headers.update({"{}".format(key):
                                                                    jsonpath.jsonpath(ret.json(), "{}".format(value))[
                                                                        0]})
        self.httpclient.session.close()

    # @file_data(PATH_JSON01)
    # def testcase02(self, data):
    #
    #     for item in data:
    #
    #         item = json.dumps(item)
    #         item = item % TestXDAPI.arg_dic
    #         item = json.loads(item)
    #         ret = self.httpclient.send_request(method=item["method"],
    #                                            url=item["url"],
    #                                            params_type=item["params_type"],
    #                                            data=item["data"])
    #         print(ret.text)
    #         self.assertEqual(jsonpath.jsonpath(ret.json(), item["assert_info"]["get_node"])[0],
    #                          item["assert_info"]["except_code"],
    #                          msg="返回code='{}'错误!".format(item["assert_info"]["except_code"]))

    # 判断参数----添加到dic字典中
    # if item.get('get_info'):
    #     for item_info in item["get_info"]:
    #         for key, value in item_info.items():
    #             TestXDAPI.arg_dic[key] = jsonpath.jsonpath(ret.json(),
    #                                                        value)[0]
    #             print(TestXDAPI.arg_dic)
    # self.httpclient.session.close()

    # @file_data(path03)
    # def testcase03(self, data):
    #     for item in data:
    #         ret = self.httpclient.send_request(method=item["method"],
    #                                            url=item["url"],
    #                                            params_type=item["params_type"])
    #         print(ret.text)
    #         self.assertEqual(jsonpath.jsonpath(ret.json(), item["assert_info"]["get_node"])[0],
    #                          item["assert_info"]["except_code"],
    #                          msg="返回code='{}'错误!".format(item["assert_info"]["except_code"]))
    #         if item.get("extract"):
    #             for key, value in item["extract"]:


if __name__ == '__main__':
    unittest.main()
