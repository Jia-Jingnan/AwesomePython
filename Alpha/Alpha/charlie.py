# coding=UTF-8

# 元组 tuple，用()表示
# 可以存在空元组，元组中可以包含任意类型的数据
a = (1, 0.2, "Go", "Python", [12, 14])
print(type(a))

# 元组里面的元素也有索引，从0开始
print(a[3])

# 元组支持切片
print(a[0:3:1])

# 元组不支持任何的修改(增删改),如果元素为列表，可以对列表里面的元素进行修改
a[4][-1] = 15
print(a)

# 如果元组中只有一个元素，请添加逗号，
b = (1)
c = (1,)
print(type(b))
print(type(c))