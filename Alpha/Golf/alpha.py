# Author:   jingnan
# Date:    2021/6/20
# Desc:  单元测试，本质就是测试代码里面的函数
# 单元测试框架  unittest + jenkins ， pytest + web -> 接口
# 接口测试框架 pytest + jenkins + allure
# 测试步骤
# 1.写用例 TestCase
# 2.执行用例 TestSuite，存储用例TestLoader 找用例，加载用例，存到TestSuite中
# 3.对比结果 断言Assert
# 4.出具测试报告 TextTestRunner

import unittest
from Alpha.Golf.bravo import MathMethod

# 写一个测试类
class TestMathMethod(unittest.TestCase): # 继承unittest中的TestCase类
    # 编写测试用例
    # 一个用例就是一个函数，不能传参数
    # 所有的用例(所有的函数都是以test开头)
    def test_add_two_positive(self):
        res = MathMethod(1, 1).add()
        print("1+1=", res)
        # 添加断言
        self.assertEqual(2,res)

    def test_add_two_zero(self):
        res = MathMethod(0, 0).add()
        print('0+0=', res)
        # msg是用例执行失败是才会显示
        self.assertEqual(1,res,"两个0相加出错了")

#
# if __name__ == '__main__':
#     unittest.main()
suite = unittest.TestSuite() # 实例化一个suite
suite.addTest(TestMathMethod('test_add_two_positive'))

with open("delta.txt", 'w+', encoding='UTF-8') as file:
    runner = unittest.TextTestRunner(stream=file, verbosity=0)
    runner.run(suite)


