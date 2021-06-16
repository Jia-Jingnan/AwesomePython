# coding=UTF-8
#

sum = 0
for i in range(1,101):
    sum += i
print("累加结果为:{}".format(sum))


def add(m, n, k):
    sum = 0
    for i in range(m, n, k):
        sum += i
    print("累加结果为:{}".format(sum))


add(1, 101, 1) #按参数位置赋值
add(m=1, k=1, n=101) # 指定参数赋值
# 有默认参数，调用时可以不用传默认参数的值，默认参数必须放到位置参数的后面


# return 函数的返回值,调用函数时会有return
# return 在函数中相当与一个结束符号，表示函数到此为止
def add_with_return(m, n, k):
    sum = 0
    for i in range(m, n, k):
        sum += i
    return sum


# 调用时需要使用一个变量取接受函数return的值
sum = add_with_return(1, 101, 1)
print(sum)


# 动态参数/不定长参数, 使用*args
def make_sandwich(a, b, c):
    print("Your sandwich made of {},{}".format(a, b))


# 不定长参数传进函数中是以元组的形式传入
def make_sandwich_with_args(*args):
    print(type(args))


make_sandwich_with_args()


# 关键字参数 key-value形式 **kwargs
def key_words(**kwargs):
    print(kwargs)
    print(type(kwargs))


# 传入关键字参数的形式，体现为字典
key_words(name="Peter")


# 传参数时位置参数优先

