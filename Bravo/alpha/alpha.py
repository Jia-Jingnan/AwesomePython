# Author:   jingnan
# Date:    2021/7/10
# Desc:

import timeit


def func():
    for i in range(10):
        print(i)


# 运行func函数100次所需要的时间
# res = timeit.Timer(func).timeit(100)
# print(res)


# 默认返回执行1千万次耗时
res = timeit.timeit('[1,2,3]')
print(res)

