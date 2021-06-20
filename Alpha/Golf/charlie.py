# Author:   jingnan
# Date:    2021/6/20
# Desc:  创建suite执行测试用例

import unittest

from Alpha.Golf.alpha import TestMathMethod

#方法一，实例化suite并添加测试用例
suite = unittest.TestSuite() # 实例化一个suite
suite.addTest(TestMathMethod('test_add_two_positive'))


#方法二：TestLoader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))

# 实例化一个runner，执行测试用例
runner = unittest.TextTestRunner()
runner.run(suite)