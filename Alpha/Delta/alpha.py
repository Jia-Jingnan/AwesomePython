# coding=UTF-8
# 题目1
for i in range(1, 6):
    print('*'*i)


# 嵌套循环,输出直角三角形
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print('')


# 输出等边三角形
for i in range(1,6): # 控制行数
    # print('第{}行'.format(i))
    # 将空格显示的表达出来，下面这个for循环控制空格
    for j in range(1,6-i):  # 控制@符号的个数
        print('@', end='')
    for k in range(1,i+1):  # 控制*的个数
        print('*',end='')

    print('')


# 输出99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('{0} * {1} = {2},'.format(i,j,i*j),end='')
    print('')


# 冒泡排序：最小的排前面，最大的排后面
# 相邻的元素相互比较， 一般最低比较 n-1次就可以完成
a = [1,23,45,4,0,7]
n = len(a)
for i in range(0, n - 1):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)


drinks = {'1': 3.5, '2': 4, '3': 2, '4': 4.5}
total = 0
choose = input("请选择1，2，3，4：")
if choose in drinks.keys():
    total += drinks[choose]
else:
    print('重新选择')



