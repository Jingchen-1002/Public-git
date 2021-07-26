# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    业务封装 showapi
"""
from api_test.util.client.httpcilent import HttpClient
import configparser
import os
from hashlib import md5
from api_test.config.read_ini import read_ini


class ShowAPI:
    """showapi接口平台"""
    # config = configparser.ConfigParser()
    # url_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config")
    # # print(url_dir)
    # config.read(url_dir + "\env.ini", encoding='utf-8')
    # URL = config.get("showapi", "URL")
    URL = read_ini("showapi", "URL")

    # def __init__(self, showapi_appid=None, secret_key=None):
    #     """
    #     :arg
    #     :param showapi_appid: 服务器id
    #     :param secret_key: 服务器密钥
    #     """
    #
    #     if showapi_appid is None:
    #         self.showapi_appid = self.config.get("showapi", "SHOWAPI_APPID")
    #     else:
    #         self.showapi_appid = showapi_appid
    #     if secret_key is None:
    #         self.secret_key = self.config.get("showapi", "SECRET_KEY")
    #     else:
    #         self.secret_key = secret_key
    #
    # def gen_signature(self, params=None):
    #     """
    #     生成签名信息
    #     :param params:
    #     :return:
    #     """
    #     buff = ""
    #     for key in sorted(params.keys()):
    #         buff += str(key) + str(params[key])
    #     buff += self.secret_key
    #     return md5(buff.encode("utf-8")).hexdigest()
    #
    # def send(self, path, method, params):
    #     """
    #     发送请求
    #     :param path: 路径
    #     :param method: 请求方法
    #     :param params: 参数
    #     :return:
    #     """
    #     params["showapi_appid"] = self.showapi_appid
    #     params["showapi_sign"] = self.gen_signature(params)
    #     try:
    #         httpclient = HttpClient()
    #         url = self.URL + "/" + path
    #         r = httpclient.send_request(method=method, url=url, params_type="FORM", data=params)
    #         httpclient.close_session()
    #         return r
    #     except Exception as e:
    #         print("调用接口失败" % e)


if __name__ == '__main__':
    ap = ShowAPI()
    pr = ap.URL
    print(pr)
