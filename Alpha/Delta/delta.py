# coding=UTF-8

# 提高类的复用性，初始化函数
class Teacher:

    def __init__(self, name, age): # 实例方法
        self.name = name
        self.age = age

    def coding(self,lines,lan='python'): # 默认参数放在最后
        # 类里面调用函数
        # self.introduce()
        print('{} coding 了 {} 行 {} 代码'.format(self.name, lines, lan))

    def cooking(self,*args):
        for item in args:
            print('会做{}'.format(item))


    def introduce(self,*args):
        self.cooking(*args)  # 可以传递多个参数
        print('I am {} and {} years old'.format(self.name, self.age))

    # 类方法
    @classmethod
    def swimming(cls):
        print('swimming')

    # 静态方法,类似普通函数，类和实例都可以调用
    @staticmethod
    def fight():
        print('fight')


teacher = Teacher('Tony Stark', 55)
teacher2 = Teacher('Peter Park', 18)
teacher.coding(10000)
teacher.introduce('python','java','vue')
teacher2.coding(100)
teacher2.introduce('python','java')


# 什么时候用初始化函数,
# 如果某个属性值是多个函数公用的，就可以用初始化函数
# 初始化函数可以默认值，初始化函数没有return返回值
#



