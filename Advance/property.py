#coding=utf-8

#property属性介绍：一种用起来像是使用实例属性一样的特殊属性
#1：定义
# class Foo:
#     def func(self):
#         pass
#
#     @property
#     def prop(self):
#         pass
#
# foo_obj = Foo()
# #调用实例方法
# foo_obj.func()
# #调用property属性
# foo_obj.prop
#
#定义时，在实例方法的基础上添加@property装饰器；并且仅有一个self参数
#调用时，无需括号

###############################################################################################################
#2：简单的实例
#以京东商城显示某个商品列表页面为例，不可能每次都把全部商品从数据库取出放到页面上显示，通过分页功能显示指定的第m条到第n条数据
#这个分页功能包括：根据用户请求的当前页和总数据条数计算出m和n；根据m和n去数据库中请求数据
# class Page:
#     def __init__(self,current_page):
#         #用户当前请求的页码
#         self.current_page =  current_page
#         #每页默认显示10条数据
#         self.per_items = 10
#
#     @property
#     def start(self):
#         val = (self.current_page - 1) * self.per_items
#         return val
#
#     @property
#     def end(self):
#         val = self.current_page * self.per_items
#         return val
#
# p = Page(10)
# start = p.start #起始值，即m
#
# end = p.end   #结束值，即n

#小结：property属性的功能是：property属性内部进行一系列的逻辑计算，最终将计算结果返回。

###############################################################################################################
#3：property属性实现有两种方式
#装饰器：在方法上应用装饰器
#类属性：在类中定义值为property对象的类属性

#装饰器方式
#在类的实例方法上应用@property装饰器
#Python中的类有经典类和新式类，新式类的属性比经典类的属性丰富，如果类继承object,那么该类是新式类

#经典类，具有一种@property装饰器
# class Goods:
#     @property
#     def price(self):
#         return 'nike'
#
# obj = Goods()
# ret = obj.price #自动执行@property装饰的price方法，并获取方法的返回值
# print(ret)


#新式类，具有三种@property装饰器
# class Goods:
#     #Python3中默认继承object类
#     @property
#     def price(self):
#         print('@property')
#
#     @price.setter
#     def price(self,value):
#         print('@property.setter')
#
#
#     @price.deleter
#     def price(self):
#         print('@property.deleter')
#
# obj = Goods()
# obj.price #自动执行@property修饰的price方法，并获取方法的返回值
# obj.price = 123 #自动执行@price.setter修饰的price方法，并将123赋值给方法的参数
# del obj.price #自动执行@price.deleter修饰的price方法

#注意
#经典类中的属性只有一种访问方式，其对应被@property修饰的方法
#新式类中的属性有三种访问方式，并分别对应了三个被@property,@方法名.setter,@方法名.deleter修饰的方法
#由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性:获取，修改，删除

class Goods(object):
    def __init__(self):
        #原价
        self.orginal_price = 100
        #折扣
        self.discount = 0.8

    @property
    def price(self):
        #实际价格 = 原价 * 折扣
        new_price = self.orginal_price * self.discount
        return new_price
    @price.setter
    def price(self,value):
        self.orginal_price = value

    @price.deleter
    def price(self):
        del self.orginal_price


obj = Goods()
print(obj.price)
ret = obj.price = 200
print(ret)
del obj.price






