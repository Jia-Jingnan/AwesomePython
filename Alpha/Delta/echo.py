# coding=UTF-8
# 继承

class RobotOne:
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walk_on_ground(self):
        print(self.name, '只能在地上走，有障碍我会摔倒')


    def robot_info(self):
        print('{}年生成的名叫{}的机器人'.format(self.year, self.name))


# 继承RobotOne
class RobotTwo():

    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walk_on_ground(self):
        print(self.name, '可以平稳行走')

    def walk_avoid_block(self):
        # 子类里面调用父类的函数,父类的函数子类都有，可以直接通过self调用
        self.robot_info()
        print('{}可以避开障碍物'.format(self.name))


# 第二代机器人
# 继承的类是否要用到初始化函数
# 父类的方法可以直接调用
# 子类重写父类的方法，调用子类的
r = RobotTwo("1990", "小王")
r.robot_info()
r.walk_on_ground()

robotOne = RobotOne("1989", "小李")
robotOne.walk_on_ground()

# 多继承
# 第三代机器人,RobotOne和RobotTwo无继承关系
# 多个继承具有两个父类的属性和方法，如果两个父类具有同名方法时，遵循就近原则，如下图函数就会先调用RobotTwo中的同名函数

class RobotThree(RobotTwo, RobotOne):

    def jump(self):
        print(self.name,'可以跳跃')


r3 = RobotThree('大王')
r3.jump()
r3.walk_on_ground()