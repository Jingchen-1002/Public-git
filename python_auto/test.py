# -*- coding:utf-8 -*-
# @Author:chenjing
# class Person(object):
#     name1 = "杰克"
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod  # 把eat方法变为类方法
#     def eat(cls):
#         print("%s is eating" % cls.name1)


# Person.name1='sss'
# Person.eat()
# d = Person('ss')
# d.eat()
# import math
#
# r = math.floor(-9.999)
# r1 = math.ceil(-9.999)
# r2 = 10 % 3
# print(r2)
"""
//获取url
var url = request.url;
//通过分割字符串，获取参数部分
param = url.split("?")[1]
//分割参数字符串，将每组参数放入数组
params = param.split("&");
//排序
params.sort();
//将参数的Key和Value分别放到两个数组中
var keys = new Array(params.length);
var values = new Array(params.length);
for(var i=0; i<params.length; i++)
{
keys[i] = params[i].split("=")[0];
values[i] = params[i].split("=")[1];
}
//按照要求拼接参数字符串
temp_arr = [];
for(var p=0;p<keys.length;p++)
{
if(keys[p]=="showapi_sign")
{
continue;
}
temp_arr.push(keys[p]+values[p])
}
var sign = temp_arr.join("")
console.log(sign)
sign = sign+"cf9ff3bbe3ae447c8af90b329b150837"
console.log(sign)
//将sign进行MD5加密，并赋值给环境变量{{sign}}
pm.environment.set("sign",CryptoJS.MD5(sign).toString())
"""
import time

"""https://route.showapi.com/64-19?com=zhongtong&nu=123456&showapi_appid=123"""
from hashlib import md5
import requests

# url = "https://route.showapi.com/64-19?com=zhongtong&nu=123456&showapi_appid=123"

# params = url.split('?')[1]
# print(params)
# param = params.split('&')
# param.sort()
# print(param)
# print(type(param))
#
# dict1 = {}
# for dic in param:
#     # print(dic)
#     key = dic.split('=')[0]
#     value = dic.split('=')[1]
#     # dict1[key] = value
#     sign = key + value

# print(dict1)
# # list = []
# # for key1 in dict1.keys():
# #     list.append(key1)
# #     for value1 in :
# #         list.append(value1)
# # print(list)
# list1 = []
# for item in dict1.items():
#     print(item)
#     list1.append(item)
# print(list1)

url = "https://route.showapi.com/64-19"

params = {
    "showapi_appid": "691912",
    "com": "zhongtong",
    "nu": "75450632975559"
}

params["showapi_time"] = time.strftime("%Y%m%d%H%M%S")

buff = ""
for key in sorted(params.keys()):
    buff += str(key) + str(params[key])
    print(buff)

print(params)

buff += "cf9ff3bbe3ae447c8af90b329b150837"

params["showapi_sign"] = md5(buff.encode("utf-8")).hexdigest()

r = requests.post(url, data=params)
print(r.text)
