# Author:   jingnan
# Date:    2021/6/30
# Desc:  ddt + unittest来进行数据的处理
# 装饰器 会在函数运行之前运行
import unittest
from ddt import ddt, data, unpack

t_data = [[1, 3],[1, 5]]

@ddt
class TestMath(unittest.TestCase):

    # @data(*t_data)  # 只能脱一层
    # def test_print_data(self, item):
    #     print(item)


    @data(*t_data)
    # 如果unpack后的参数 少于5个，推荐使用unpack
    # 要注意参数不对等的情况，提供对应个数的参数来接收数据
    # 如果要对字典进行unpack，参数要与字典的key对应
    @unpack
    def test_print_data_2(self, a, b):
        print('a', a)
        print('b', b)




