# coding=utf-8
#############################################################
# 1.单独调用父类的方法
# print('多继承使用类名，__init__发生的状态')
#
#
# class Parent(object):
#     def __init__(self, name):
#         print('parent的init开始调用')
#         self.name = name
#         print('parent的init结束被调用')
#
#
# class Son1(Parent):
#     def __init__(self, name, age):
#         print('Son1的init开始被调用')
#         self.age = age
#         Parent.__init__(self, name)
#         print('Son1的init结束被调用')
#
#
# class Son2(Parent):
#     def __init__(self, name, gender):
#         print('Son2的init开始被调用')
#         self.gender = gender
#         Parent.__init__(self, name)
#         print('Son2的init结束被调用')
#
#
# class Grandson(Son1, Son2):
#     def __init__(self, name, age, gender):
#         print('Grandson的init开始被调用')
#         Son1.__init__(self, name, age)
#         Son2.__init__(self, name, gender)
#         print('Grandson的init结束被调用')
#
#
# gs = Grandson('grandson', 12, '男')
# print('姓名:{}'.format(gs.name))
# print('岁数:{}'.format(gs.age))
# print('性别:{}'.format(gs.gender))

#############################################################
#2.多继承中super调用所有父类的被重写的方法
print('多继承使用super().__init__发生的状态')

class Parent(object):
    def __init__(self,name,*args,**kwargs):
        print('Parent的init开始被调用')
        self.name = name
        print('Parent的init结束被调用')


class Son1(Parent):
    def __init__(self,name,age,*args,**kwargs):
        print('Son1的init开始被调用')
        self.age = age
        super().__init__(name,*args,**kwargs)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self,name,gender,*args,**kwargs):
        print('Son2的init开始被调用')
        self.gender = gender
        super().__init__(name,*args,**kwargs)
        print('Son2的init结束被调用')


class Grandson(Son1,Son2):
    def __init__(self,name,age,gender):
        print('Grandson的init开始被调用')
        super().__init__(name,age,gender)
        print('Grandson的init结束被调用')

print(Grandson.__mro__)
gs = Grandson('jack', 12, '男')
print('姓名:{}'.format(gs.name))
print('年龄:{}'.format(gs.age))
print('性别:{}'.format(gs.gender))
print('多继承使用super().__init__发生的状态\n')

