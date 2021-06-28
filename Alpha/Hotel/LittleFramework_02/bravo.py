# Author:   jingnan
# Date:    2021/6/26
# Desc:

# test_http, 测试用例
import unittest
from Alpha.Hotel.LittleFramework.alpha import HttpRequest
from Alpha.Hotel.LittleFramework.delta import GetData


class TestHttp(unittest.TestCase):

    def __init__(self, methodName, url, method, data, expected):
        super(TestHttp, self).__init__(methodName) # 保留父类的方法
        self.url = url
        self.method = method
        self.data = data
        self.expected = expected

    def setUp(self):
        pass

    #用例 1
    def test_api(self):
            res = HttpRequest().request(self.url, self.data, self.method, getattr(GetData, 'Cookie'))
            if res.cookies:
                setattr(GetData, 'Cookie', res.cookies)
            try:
                self.assertEqual(self.expected, res.json()['status'])
            except AssertionError as e:
                print('test_login_normal error is {}'.format(e))
                raise e
            print(res.status_code)
            print(res.text)

    def tearDown(self):
        pass
