# -*- coding:utf-8 -*-
# @Author:chenjing
import datetime
import json
from api_test_auto.util.request_util import RequestUtil

from api_test_auto.util.db_util import MysqlDb


class ApiTestCase:

    def loadAllCaseByApp(self, app):
        """
        根据app加载全部测试用例
        :return: result
        """
        print('loadAllCaseByApp')
        my_db = MysqlDb()
        sql = "select * from `case` where app='{0}'".format(app)
        result = my_db.query(sql)
        return result

    def findCaseById(self, case_id):
        """
        根据id找测试用例
        :param case_id:
        :return:
        """
        print('findCaseById')
        my_db = MysqlDb()
        sql = "select * from `case` where id='{0}'".format(case_id)
        result = my_db.query(sql, state='one')
        return result

    def loadConfigByAppAndKey(self, app, key):
        """
        根据app和key加载配置
        :param app:
        :param key:
        :return:
        """
        print('loadConfigByAppAndKey')
        my_db = MysqlDb()
        sql = "select * from `config` where app='{0}' and dict_key='{1}'".format(app, key)
        result = my_db.query(sql, state='one')
        return result

    def updateResultByCaseId(self, response, is_pass, msg, case_id):
        """
        根据测试用例id，更新响应内容和测试内容
        :param response:
        :param is_pass:
        :param msg:
        :param case_id:
        :return:
        """
        print('updateResultByCaseId')
        my_db = MysqlDb()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_time)
        if is_pass:
            sql = "update `case` set response='{0}',pass='{1}',msg='{2}',update_time='{3}'where id='{4}'".format(
                "", is_pass, msg, current_time, case_id)
        else:
            sql = "update `case` set response= '{0}' ,pass='{1}',msg='{2}',update_time='{3}'where id='{4}'".format(
                str(response), is_pass, msg, current_time, case_id)
        rows = my_db.execute(sql)
        return rows

    def runAllCase(self, app):
        """
        执行全部用例
        :param app:
        :return:
        """
        print('runAllCase')
        # 读取域名
        api_host_obj = self.loadConfigByAppAndKey(app, "host")
        # 读取全部用例
        results = self.loadAllCaseByApp(app)
        for case in results:
            print(case)
            if case['run'] == 'yes':
                try:
                    # 执行
                    response = self.runCase(case, api_host_obj)
                    # 断言
                    assert_msg = self.assertResponse(case, response)
                    # 响应结果添加到数据库
                    rows = self.updateResultByCaseId(response, assert_msg['is_pass'], assert_msg['msg'], case['id'])
                    print('rows={0}'.format(rows))
                except Exception as e:
                    print('用例id={0}，标题title={1}'.format(case['id'], case['title'], e))
        self.sendTestReport(app)

    def runCase(self, case, api_host_obj):
        """
        执行单个用例
        :param case:
        :param api_host_obj:
        :return:
        """
        print("runCase")
        headers = json.loads(case['headers'])
        body = json.loads(case['request_body'])
        method = case['method']
        req_url = api_host_obj['dict_value'] + case['url']

        # 判断前置
        if int(case['pre_case_id']) > -1:
            print("前置条件")
            pre_case_id = case['pre_case_id']
            pre_case = self.findCaseById(pre_case_id)
            # 递归操作
            pre_response = self.runCase(pre_case, api_host_obj)
            pre_assert_msg = self.assertResponse(pre_case, pre_response)
            if not pre_assert_msg["is_pass"]:
                pre_response['msg'] = "前置条件不通过"+pre_response['msg']
                return pre_response
            pre_fields = json.loads(case['pre_fields'])
            for pre_field in pre_fields:
                print(pre_field)
                if pre_field['scope'] == 'header':
                    for header in headers:
                        field_name = pre_field['field']
                        if header == field_name:
                            # 替换headers
                            field_value = pre_response['data'][field_name]
                            headers[field_name] = field_value
                elif pre_field['scope'] == 'body':
                    print('替换body')
        print(headers)
        # 请求操作
        res_request = RequestUtil()
        response = res_request.request(req_url, method, headers=headers, param=body)
        return response

    def assertResponse(self, case, response):
        """
        断言响应内容，更新用例执行情况
        :param case:
        :param response:
        :return:
        """
        print('assertResponse')
        assert_type = case['assert_type']
        expect_result = case['expect_result']
        is_pass = False
        # 判断状态码
        if assert_type == 'code':
            response_code = response['code']
            if int(expect_result) == response_code:
                is_pass = True
                print('通过！')
            else:
                print('失败！')
                is_pass = False
        # 判断数组长度
        elif assert_type == 'data_json_array':
            data_array = response['data']
            if data_array is not None and isinstance(data_array, list) and len(data_array) > int(expect_result):
                is_pass = True
                print('通过！')
            else:
                print('失败！')
                is_pass = False
        elif assert_type == 'data_json':
            data = response['data']
            if data is not None and isinstance(data, dict) and len(data) > int(expect_result):
                is_pass = True
                print('通过！')
            else:
                print('失败！')
                is_pass = False
        msg = "模块：{0},标题：{1},断言类型：{2},响应：{3}".format(case['module'], case['title'], assert_type, response['msg'])
        # 拼接
        assert_msg = {"is_pass": is_pass, "msg": msg}
        return assert_msg

    def sendTestReport(self, app):
        """
        发送测试报告
        :param app:
        :return:
        """
        print('sendTestReport')


if __name__ == '__main__':
    print('main')
    test = ApiTestCase()
    # result = test.loadAllCaseByApp("小滴课堂")
    result = test.findCaseById('1')
    print(result)
