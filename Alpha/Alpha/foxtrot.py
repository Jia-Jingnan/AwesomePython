# coding=UTF-8

# 控制语句，分支分流， 循环语句 for while

# if
#   print()

# 判断语句  if .(条件为比较，逻辑，成员均可)..elif ... else
age = 18
if age > 20:
    print("成年")  # if后面的语句满足条件，运算结果是true，就会执行他的子语句，2，空数据=false，非空数据=true
else:              # else后面不能添加条件
    print("未成年")


# 判断语句3
if age > 10:
    print()
elif 18 > age > 10:         # elif可以有多个
    print()
else:
    print()

# input()函数，从控制台获取数据，获取的数据都是字符串类型
age = input("请输入年龄：")
print(type(age))

