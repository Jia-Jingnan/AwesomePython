# Author:   jingnan
# Date:    2021/6/21
# Desc:

import unittest
class TestHttp(unittest.TestCase):

    def setUp(self):
        pass


    def __init__(self, methodName, url, data, method, expected):
        super(TestHttp.self).__init__(methodName)  # 保留父类的__init__方法
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected

    def test_api(self):
        pass


    def tearDown(self):
        pass