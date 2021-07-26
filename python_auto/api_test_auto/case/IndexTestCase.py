# -*- coding:utf-8 -*-
# @Author:chenjing
import unittest

import requests

from api_test_auto.util.request_util import RequestUtil

host = 'https://api.xdclass.net'


class IndexTestCase(unittest.TestCase):

    def testIndexCategory(self):
        """
        首页
        :return:
        """
        request = RequestUtil()
        url = host + '/pub/api/v1/web/all_category'
        response = request.request(url, 'get')
        self.assertEqual(response['code'], 0, msg="业务状态不正常")
        self.assertTrue(len(response['data']) > 0, '分类列表为空')

    def testIndexCard(self):
        """
        视频卡片
        :return:
        """
        request = RequestUtil()
        url = host + '/pub/api/v1/web/index_card'
        response = request.request(url, 'get')
        self.assertEqual(response['code'], 0, msg='业务状态不正常')
        self.assertTrue(len(response['data']) > 0, '视频卡片列表为空')
        video_card_title = response['data']
        for card in video_card_title:
            print(type(card))
            self.assertTrue(len(card['title']) > 0, "card is null id=" + str(card['id']))

    def testIndexVideoDetail(self):
        """
        视频详情
        :return:
        """
        request = RequestUtil()
        url = host + '/pub/api/v1/web/video_detail?video_id=53'
        response = request.request(url, 'get')
        self.assertEqual(response['code'], 0, msg='业务状态不正常')
        self.assertTrue(len(response['data']) > 0, '视频详细信息为空')

    def testIndexWebLogin(self):
        """
        用户登录
        :return:
        """
        request = RequestUtil()
        url = host + '/pub/api/v1/web/web_login'
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"iphone": "13113777555", "pwd": "1234567890"}
        response = request.request(url, 'post', param=data, headers=headers)
        self.assertEqual(response['code'], 0, msg="业务状态不正常")

    def IndexUserInfo(self):
        """
        用户信息
        :return:
        """
        request = RequestUtil()
        url = host + '/pub/api/v1/web/user_info'
        headers = {"token": "11"}
        response = request.request(url, 'get', headers=headers)
        self.assertEqual(response['code'], 0, msg='业务状态不正常')
        self.assertTrue(len(response['data']) > 0, msg="响应数据为空")


if __name__ == '__main__':
    unittest.main(verbosity=2)
