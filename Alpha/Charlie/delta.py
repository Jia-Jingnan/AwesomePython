# coding=UTF-8
import os


# Python中的异常处理
# 异常：在代码运行过程中遇到的任何错误error
# 异常处理：对代码中的异常进行处理
# FileExistsError， OSError， NameError，
try:
    os.mkdir("bravo")   # FileExistsError
except FileExistsError:  # 精确捕获异常
    # 初级异常处理
    print('捕获异常，待处理')


try:
    os.mkdir("bravo")   # FileExistsError
except Exception:      # 扩大捕捉的异常范围
    print('捕获异常，待处理')

print('可以运行')

# 指明处理某个错误，精确到具体的错误类型
# 处理某种类型的错误，扩大范围
# 有错就抓

# 异常要捕获，还要有处理
try:
    os.mkdir('bravo')
except OSError as c:  # 把错误存到变量c中
    print("捕获异常,待处理")
    print("错误为：{}".format(c))  # 打印出变量
else:    # 跟try下面的代码是一起的，你好我就好，你不好我就不好
    print('这是else语句部分')
