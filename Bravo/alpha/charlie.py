# Author:   jingnan
# Date:    2021/7/11
# Desc: 字典和集合


# 字典和集合定义
se = set()  # 空集合

set1 = {1,2,3} # 没有key，不存在重复元素

# 带有重复元素的列表
li = [1,1,3,3,2,23,34,23]
# 列表去重的方法，先转换成集合,在转换成列表
print(list(set(li)))

# 集合添加数据,集合是可变类型的数据
se.add('Thor')
print(se)
# 集合删除
se.remove('Thor')
print(se)

# 集合的交集并集
# 集合的更新
se.update((11,22,33))  # 等同于列表的extend方法
print(se)

# 集合清空
se.clear()

# 集合复制
se.copy()

dic = {}  # 空字典



