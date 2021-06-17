# coding=UTF-8

# python 操作文件 txt，xml等

# 定义一个file对象
file = open("juliet.txt")

# 读取file中的内容
context = file.read()
print(context)

# 读取文件的模式 mode,共12种，默认是r,只读模式
# r只读, w只写, a追加
# r+, w+, a+ 可读可写
# rb, rb+, wb, wb+, ab, ab+

# r+，可读可写，写的位置与光标位置有关，先写的话一开始光标在起始位置，写入的内容在最前面，先读，此时光标在末尾
# 再次写入时，只会在最后面写入内容，读写跟着光标走
file_kilo = open("kilo.txt","r+")
context_kilo = file_kilo.read() # read()中可以填入读的字符的个数read(5)，只读5个字符，光标移动到第5个字符
print(context_kilo)
file_kilo.write("kilo")
print(context_kilo)

# 写入中文要注意编码格式,参数中加入，encoding="utf-8"
# 读和写分开操作，否则造成写入中文乱码
file_lima = open("lima.txt", "r+", encoding="utf-8")
file_lima.write("这是写入的一串中文")

# w 只写 硬要去读就会报错， w+ 可读可写
# 如果文件存在就直接清空重写写入，如果文件不存在，则新建一个文件，然后写入，慎用！！！！
file_mike = open("mike.txt", "w+", encoding="utf-8")
file_mike.write("第二次写入中文，这次会直接清空原内容，再写入")

# 移动光标操作？

# a 追加，光标移动后才有意义，如果文件存在就直接追加写在后面，如果文件不存在则新建一个文件写入内容
# 换行的话要手动添加换行符 "\n"
file_nove = open("november.txt", "a", encoding="utf-8")
file_nove.write("第三次写入中文，这次是追加")

# 重点掌握 r, a
# 按行读取
file_oscar = open("oscar.txt", "a", encoding="utf-8")
# print(file_oscar.readline())

# print(file_oscar.readline(2))

# 读取多行，返回列表
# print(file_oscar.readlines())

file_oscar.writelines(["777\n","999"])



