# Author:   jingnan
# Date:    2021/7/11
# Desc:  命名元组

# 命名元组
tu = ('thor', 1800, 'M')


# 创建命名元组
from collections import namedtuple

# 先创建一个namedtuple对象，设定元组的命名
student_info = namedtuple('student_info', ['name', 'age', 'gender'])
# 给对象赋值
tu = student_info('thor', 1800, 'M')
print(tu)

# 取值
print(tu.name)
print(tu.gender)
print(type(tu))

