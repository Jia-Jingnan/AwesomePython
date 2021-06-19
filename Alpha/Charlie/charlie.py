# coding=UTF-8

import os

# 路径的获取，获取工作目录，具体到最后一级目录
path = os.getcwd()
print("当前路径为：{0}".format(path))

# 路径获取2,获取当前文件的绝对路径，具体到文件
path2 = os.path.realpath(__file__)
print("路径2：{}".format(path2))

# 路径3：如何拼接路径
new_path_1 = os.getcwd() + "/python1"
print(new_path_1)
# 新建文件夹
# os.mkdir(new_path_1)

# 路径拼接2，不用加/，使用这个路径创建目录时，要注意上一级路径存在，不能跨多级新建
new_path_2 = os.path.join(os.getcwd(), "python2", 'sub1')
print(new_path_2)

# 判断路径是否是文件，返回true 或false
os.path.isfile()
# 判断是否为目录
os.path.isdir(os.getcwd())


# 罗列出当前路径下的所有文件和目录
print(os.listdir(os.getcwd()))


# 给定一个路径，打印出所有路径
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.patg.join(os.getcwd(),path))
        print('{0}还需要进一步处理'.format(path))

    else:
        print('无尽的目录', os.path.join(os.getcwd(), path))