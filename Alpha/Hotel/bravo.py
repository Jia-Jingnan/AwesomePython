# Author:   jingnan
# Date:    2021/6/22
# Desc:

# eval()把数据类型转换为原本的数据类型
s = '{"age": 18}'

print(eval(s), type(s), type(eval(s)))