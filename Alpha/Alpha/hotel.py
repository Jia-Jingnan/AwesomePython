# coding=UTF-8

# while控制循环
# 语法：while 条件表达式：
        # 代码块

# 执行规律：先判断while 后面的条件表达式是否成立
# 如果为true 执行代码块，执行完毕之后，继续判断，如果为true，执行代码块
# 否则不进入代码块
# 条件，空数据为false，非空数据为true

i = 0
sum = 0
while i < 101:
    sum += i
    i += 1
print(sum)

# while与if搭配使用， break ，contiue
