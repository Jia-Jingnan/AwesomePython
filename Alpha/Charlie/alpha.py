# coding=UTF-8

# 相对路径，绝对路径

import os

# 新建目录，新建文件夹
# os.mkdir("bravo")

# 跨级新建目录,确保上一级(bravo)必须存在
# 相对路径
# os.mkdir("bravo/alpha")

# 删除目录,删除文件也是一级一级的删除，不推荐一次性删除
os.rmdir("bravo/alpha")

# 新建文件 open，删除文件如何操作？

