# Author:   jingnan
# Date:    2021/6/26
# Desc:

# test_suite, 测试用例加载，执行，生成报告
import unittest
from Alpha.Hotel.LittleFramework.bravo import TestHttp
from Alpha.Hotel.LittleFramework.HTMLTestRunner_Chart import HTMLTestRunner

data = [
    {'url': 'http://localhost:8089/user/login.do', 'method': 'post', 'data': {"username": "admin", "password": "admin"}, 'excepted': '0'},
    {'url': 'http://localhost:8089/user/login.do', 'method': 'post', 'data': {"username": "admin", "password": "admin1"}, 'excepted': '1'},
    {'url': 'http://localhost:8089/user/login.do', 'method': 'post', 'data': {"username": "admin1", "password": "admin"}, 'excepted': '1'},
]

suite = unittest.TestSuite()
# 类名加载用例
loader = unittest.TestLoader()
# 将三个数据的用例添加到suite中，每一条用例的数据都不一样
for item in data:
    # 实例化TestHttp，将data中的数据赋值给实例化的TestHttp，然后加载进suite中
    suite.addTest(TestHttp('test_api', item['url'], item['data'], item['method'], int(item['excepted'])))  # 实例的方法加载用例


# 执行
with open("echo.html", 'wb') as file:
    runner = HTMLTestRunner(stream=file, verbosity=1, title=None, description=None)
    runner.run(suite)