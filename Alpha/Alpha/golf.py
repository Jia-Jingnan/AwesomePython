# coding=UTF-8

# 循环 for while，可以循环的数据类型有 字符串，元组，列表，字典，集合
# for循环遍历a中的元素，把每一个元素赋值给item
# for循环的循环次数有元素的个数决定
a = 'Hello'
for item in a:
    print(item)

# 字典类型的数据遍历访问的是key
b = {"name": "Tony", "age": 59}
for i in b:
    print(b[i])
# 字典的一些函数
print(b.values())  # 获取字典里的所有value
print(b.keys())    # 获取字典里的所有key
# 可以单独获取value和可以

sum = 0
c = [5, 6, 9, 3]
for item in c:
    sum += item
    print(sum)

# range()函数
# range(m,n,k) m为头，n为尾，k为步长，默认为1，取头不取尾,头默认为0
range(1, 5, 1)

for item in range(3):
    print(item)

l = [5, 6, 7, 9, 4]
for item in range(len(l)):
    print(l[item])

sum = 0
for item in range(101):
    sum += item

print(sum)

# 嵌套循环
