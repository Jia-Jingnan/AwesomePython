# coding=UTF-8


# Python 类的语法 关键字 class
# class 类名:
#     类属性 ：放在类里面的变量值
#     类方法 ：放在类里面的方法
# 类名的规范是，数字字母下划线组成，首字母大写，不能以数字开头，驼峰命名

class Friend:
    # 类属性
    height = 175
    weight = 130
    money = 500


    # 类方法,方法都必须要带self这个参数，self是固定的占坑符号
    def cooking(self):
        print('会做饭')


    def print_self(self):
        print(self)


# 实例/对象 具体的一个例子，类名()
# 实例里面据类的所有属性和方法的使用权限
friend = Friend()
print(friend.height)
print(friend.cooking())
friend.print_self()


