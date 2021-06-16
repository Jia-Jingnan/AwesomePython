# coding=UTF-8
# 字典 dict {} 大括号表示
# 字典相关操作
# 空字典,字典的value可以包含任意数据，存储方式key：value方式，即键值对方式存储，用逗号来分割
a = {}
print(a)
print(type(a))
# 没有切片,可以根据key获取value，字典没有索引，字典是无序的
a = {"Peter Park": "SpriderMan","Tony Stark": "IronMan","Live Place": "NewYork","age": 11}

print(a)

# 字典取值,字典[key]
print(a["age"])

# pop()删除函数，指定key删除,并返回删除的值
res = a.pop("age")
print(a)
print(res)

# 新增 字典[newKey] = newValue,newKey是字典里不存在的key
a["thor"] = "God of Thunder"
print(a)

# 修改 字典[oldKey] = newValue
a["thor"] = 18
print(a)

# 字典里的key必须是唯一的


