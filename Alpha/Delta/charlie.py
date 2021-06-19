# coding=UTF-8

# 类与对象
# 命令规范：首字母大写，驼峰命名，简单明了
# 类的概念，具有某一类共同属性和特性的事物
# 类一般包含 属性以及方法

class Teacher:
    name = 'Tony Stark'
    age = 55


    def coding(self):
        print('coding')


    def cooking(self):
        print('cooking')

    # 类方法
    @classmethod
    def swimming(cls):
        print('swimming')

    # 静态方法,类似普通函数，类和实例都可以调用
    @staticmethod
    def fight():
        print('fight')


# 类里面的方法有三种
# 实例方法，意味着这个方法只能由实力来调用
t = Teacher()
t.cooking()
# 不推荐此种方式调用实例方法
Teacher.cooking(t)

# 类方法只能由类调用,不需要创建实例
t.swimming()

# 类调用 类方法
Teacher.swimming()

# 静态方法可以被实例或者类调用
t.fight()
Teacher.fight()

# 实例方法self, 类方法cls，静态方法
# 静态方法和类方法不可以调用类里面的属性值，如果要参数，请自行传递参数
# 什么时候定义静态方法和类方法？
# 当某个函数与其他的类函数，类属性没有任何关系的时候就可以定义类方法和静态方法
