# -*- coding:utf-8 -*-
# @Author:chenjing
import unittest
from api_test.lib.showapi import ShowAPI


class TestShowApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.api = ShowAPI()

    def test_64_19(self):
        params = {
            "com": "zhongtong",
            "nu": "75450632975559"
        }
        ret = self.api.send(method="post", path="64-19", params=params)
        print(ret.text)
        self.assertEqual(ret.json()["showapi_res_code"], 0, msg="业务状态不正常!")


if __name__ == '__main__':
    unittest.main()
