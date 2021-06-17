# coding=UTF-8

# 全局变量和局部变量
# 作用范围不同,函数的局部变量只能作用于函数,全局变量在模块里面都能调用
# 当全局变量和局部变量同名同时存在时，优先选择局部变量
# 声明一个全局变量
global a

#
num = input("请输入4位数:")
for item in num:
    print(item)
    item = int(item)


# 怎么查看函数
# 怎么引入不同的模块
a = [1, 2, 3, 4]
print(a.pop())


# 导入方式 import
import email.mime.base
# 一层一层的拨开
# 导入方式from...import...

# 引入自定义的函数
import Alpha.Bravo.bravo

Alpha.Bravo.bravo.add(1, 100, 1)

# 引入方式二
from Alpha.Bravo.bravo import add
add(1, 101, 1)


# 主程序执行入口
if __name__ == '__main__':
    print("I am IronMan")
    add(1, 101, 1)
    print("Done！")