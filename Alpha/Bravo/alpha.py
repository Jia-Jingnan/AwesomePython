# coding=UTF-8

# python内置函数
# print input len type str int float list range
# pop append insert keys split replace strip values remove clear

# 总结下函数的特点
# 可以重复使用

# 定义函数的语法
# def 关键字
# 函数命名的规范:小写字母，不能以数字开头，不同的字母之间用下划线隔开
# def 函数名(参数1，参数2...):
    # 函数体：实现功能

# 调用：函数名()

# 定义函数，name为实参
def who_am_i(name):
    print("I am {}".format(name))


# 调用函数
who_am_i("Jingnan")

# 默认参数,name="jingnan",给出参数的默认值


def summary():
    sum = 0
    i = 0
    while i < 101:
        sum += i
        i += 1
    print(sum)


summary()

