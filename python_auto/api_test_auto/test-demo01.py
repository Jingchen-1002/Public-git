# -*- coding:utf-8 -*-
# @Author:chenjing
import requests

# response = requests.get('')

# data = {
#     "video_id": 53
# }
#
# response = requests.get('', data)

# data = {
#     "pthone": "",
#     "pwd": ""
# }
# json = {
#     "pp": "",
#     "oo": ""
# }
# post 提交有两点传参： data 和 json

# Content-Type:application/x-www-form-urlencoded
# response = requests.post("url", data=data)
# # Content-Type:application/json
# response1 = requests.post("url", json=json)
# print(response.text)

# headers = {"token": "111@DDEDEFEFe"}
# requests.get("url",headers=headers)

# response = requests.post("url", data={"video_id": 45}, headers=headers)

# print(response.text)

# result = requests.get('https://api.xdclass.net/pub/api/v1/web/video_detail?video_id=53')
# print(result.text)

result = requests.get("https://bms-test.sheencity.com/auth/login")
# print(result.text)
# print(result.status_code)


