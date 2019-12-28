#coding=utf-8

#property属性-应用
###############################################################################################################
#1.私有属性添加getter和setter方法
# class Money(object):
#     def __init__(self):
#         self.__money = 0
#
#     def getMoney(self):
#         return self.__money
#
#     def setMoney(self,val):
#         if isinstance(val,int):
#             self.__money = val
#         else:
#             print('error:value is not interger')
#
# a = Money()
# ret = a.getMoney()
# print(ret)
# a.setMoney(100.4)


###############################################################################################################
#2.使用property升级getter和setter方法
# class Money(object):
#     def __init__(self):
#         self.__money = 0
#
#     def getMoney(self):
#         return self.__money
#
#     def setMoney(self,val):
#         if isinstance(val,int):
#             self.__money = val
#         else:
#             raise TypeError
#
#     money = property(getMoney,setMoney)
#
# a = Money()
# a.money = 100
# print(a.money)


###############################################################################################################
#3使用property取代getter和setter方法
#重新实现一个属性的设置和读取方法，可做边界判定
class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,val):
        if isinstance(val,int):
            self.__money = val
        else:
            raise TypeError

    @money.deleter
    def money(self):
        del self.__money


a = Money() #实例化
a.money = 100 #调用setter
a.money #调用本身函数
del a.money #调用deleter