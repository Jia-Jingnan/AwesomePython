# coding=UTF-8
# Python中的数据类型，列表，元祖，字典，运算符
# 列表
# 列表可以包含空列表,可以包含任何类型的数据,列表里面的元素根据逗号分割
# 列表的操作
# 获取列表中的元素，通过索引确定各元素的位置
a = [1,0.02,"Hello",'Python']
print(a[-1])
# 列表的切片 列表[起始索引，结束索引，步长]
# 获取偶数位
print(a[::2])

# 什么时候会用到列表？
# 列表的作用？用来存储数据，列表中存储的数据是同一个类型时使用列表

# 往列表中追加元素,append()函数,默认追加在末尾，可以追加任何类型的数据，只能追加一个元素
a.append("晴天")
print("a列表的值为:{}".format(a))

# 往列表中插入元素,insert()函数
a.insert(1,"Tony Stark")
print("Insert后a的值为：{}".format(a))

# 删除最后一个元素 pop()函数,传入索引值可以删除具体位置的元素,并返回被删除的值
a.pop()
print("Pop后a的值为：{}".format(a))

# 删除指定的元素 remove()函数，传入元素的值
a.remove(1)
print("remove后a的值为：{}".format(a))

# 运算符
# 赋值
