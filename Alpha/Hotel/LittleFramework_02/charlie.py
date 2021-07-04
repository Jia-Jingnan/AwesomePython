# Author:   jingnan
# Date:    2021/6/26
# Desc:

# test_suite, 测试用例加载，执行，生成报告
import unittest
from Alpha.Hotel.LittleFramework_02.bravo import TestHttp
from Alpha.Hotel.LittleFramework_02.HTMLTestRunner_Chart import HTMLTestRunner



# 使用ddt时，必须使用load方式加载用例
suite = unittest.TestSuite()
# 类名加载用例
loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromTestCase(TestHttp))

# 执行
with open("echo.html", 'wb') as file:
    runner = HTMLTestRunner(stream=file, verbosity=1, title=None, description=None)
    runner.run(suite)




