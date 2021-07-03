# Author:   jingnan
# Date:    2021/6/26
# Desc:

# test_http, 测试用例
import unittest
from Alpha.Hotel.LittleFramework.alpha import HttpRequest
from Alpha.Hotel.LittleFramework.delta import GetData
from ddt import ddt, data
from Alpha.Hotel.LittleFramework_02.excel_util import ExcelUtil


# 实例化对象
bravo = ExcelUtil('bravo.xlsx', 'test')
# 调用函数
cases = bravo.get_param(case_ids=[1])

print(cases)

@ddt
class TestHttp(unittest.TestCase):

    # 使用ddt，不在需要超继承
    # 超继承
    # def __init__(self, methodName, url, method, data, expected):
    #     super(TestHttp, self).__init__(methodName) # 保留父类的方法
    #     self.url = url
    #     self.method = method
    #     self.data = data
    #     self.expected = expected

    def setUp(self):
        pass

    #用例 1
    @data(*cases)
    def test_api(self, param):
            res = HttpRequest().request(param['url'], eval(param['data']), param['method'], getattr(GetData, 'Cookie'))
            if res.cookies:
                setattr(GetData, 'Cookie', res.cookies)
            try:
                self.assertEqual(param['excepted'], res.json()['status'])
            except AssertionError as e:
                print('test_login_normal error is {}'.format(e))
                raise e
            print(res.status_code)
            print(res.text)

    def tearDown(self):
        pass

