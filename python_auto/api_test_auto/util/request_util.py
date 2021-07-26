# -*- coding:utf-8 -*-
# @Author: chenjing
import requests

"""
    工具类requests
"""


class RequestUtil:

    def __init__(self):
        pass

    def request(self, url, method, headers=None, param=None, content_type=None):
        """
        通用请求
        :param url:
        :param method:
        :param headers:
        :param param:
        :param content_type:
        :return:
        """
        try:
            if method == 'get':
                result = requests.get(url=url, params=param, headers=headers).json()
                return result
            elif method == 'post':
                if content_type == "application/json":
                    result = requests.post(url=url, json=param, headers=headers).json()
                    return result
                else:
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return result
            else:
                print("http method error!")


        except Exception as e:
            print('http request error :{}'.format(e))


if __name__ == '__maain__':
    # url = "https://api.sheencity.com/v3/bms/users?offset=0&limit=10&order=DESC&sort=created_at"
    # r = RequestUtil()
    # result = r.request(url,'get')
    # print(result)

    url = "https://api.xdclass.net/pub/api/v1/web/web_login"
    r = RequestUtil()
    data = {
        "phone ": "13484848484",
        "pwd": "12121212"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    result = r.request(url, 'post', param=data, headers=headers)
    print(result)
