# -*- coding:utf-8 -*-
# @Author:chenjing
"""
    封装requests
"""
import requests
import json
from api_test.util.logger import log


class HttpClient:

    def __init__(self):
        """构造session"""
        self.session = requests.session()

    def send_request(self, method, url, params_type="FORM", data=None, headers=None, **kwargs):
        """
        :arg
        :param method: 请求方法
        :param url: url
        :param params_type: 传参形式
        :param data: 传参类型
        :param headers: 请求头
        :param kwargs: 字典
        :return:
        """
        # 转大写
        method = method.upper()
        params_type = params_type.upper()

        # 判断是否为字典
        if isinstance(data, str):
            data = json.loads(data)
            # data = json.dumps(data)
        if "GET" == method:
            log.info(
                "请求方法:{0},请求url：{1},请求头headers：{2}，请求参数：{3}，请求格式：{4}".format(method, url, headers, data, params_type))
            response = self.session.request(method=method, url=url, params=data, headers=headers, **kwargs)
        elif "POST" == method:
            log.info(
                "请求方法:{0},请求url：{1},请求头headers：{2}，请求参数：{3}，请求格式：{4}".format(method, url, headers, data, params_type))
            if params_type == 'FORM':  # 表单形式
                response = self.session.request(method=method, url=url, data=data, headers=None, **kwargs)
            elif params_type == 'JSON':  # json形式
                response = self.session.request(method=method, url=url, json=data, headers=None, **kwargs)
        elif "DELETE" == method:
            log.info(
                "请求方法:{0},请求url：{1},请求头headers：{2}，请求参数：{3}，请求格式：{4}".format(method, url, headers, data, params_type))
            if params_type == 'FORM':  # 表单形式
                response = self.session.request(method=method, url=url, data=data, headers=None, **kwargs)
            elif params_type == 'JSON':  # json形式
                response = self.session.request(method=method, url=url, json=data, headers=None, **kwargs)
        elif "PUT" == method:
            log.info(
                "请求方法:{0},请求url：{1},请求头headers：{2}，请求参数：{3}，请求格式：{4}".format(method, url, headers, data, params_type))
            if params_type == 'FORM':  # 表单形式
                response = self.session.request(method=method, url=url, data=data, headers=None, **kwargs)
            elif params_type == 'JSON':  # json形式
                response = self.session.request(method=method, url=url, json=data, headers=None, **kwargs)
        else:
            log.error(
                "请求方法:{0},请求url：{1},请求头headers：{2}，请求参数：{3}，请求格式：{4}".format(method, url, headers, data, params_type))
            raise ValueError("request method '{}' error ".format(method))
        return response

    # 直接调用
    def __call__(self, method, url, params_type=None, data=None, headers=None, **kwargs):
        return self.send_request(method, url, params_type, data, headers, **kwargs)

    # 关闭session
    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    pass
