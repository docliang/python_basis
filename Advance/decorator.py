# def w1(func):
#     def inner():
#         print("---正在验证权限---")
#         func()
#     return inner
#
#
#
#
# #f1 = w1(f1)
# @w1
# def f1():
#     print("---f1---")
#
# @w1
# def f2():
#     print("---f2---")
#
# f1()
# f2()
#
# def makebold(fn):
#    def wrapped():
#        print('--1--')
#        return "<b>" + fn() + "</b>"
#
#    return wrapped
#
# def makeitalic(fn):
#    def wrapped():
#        print('--2--')
#        return "<i>" + fn() + "</i>"
#
#    return wrapped
#
# @makebold
# def test1():
#    return "hello 1"
#
# @makeitalic
# def test2():
#    return "hello 2"
#
#
# @makebold
# @makeitalic
# def test3():
#    return "hello 3"
#
# m=test1()
# n=test2()
# k=test3()
# print(m)
# print(n)
# print(k)

# print(test1())
# print(test2())
# print(test3())
#
# def deco1(func):
#     def deco2():
#         print('正在检测')
#         print('检测成功')
#         func()
#     return deco2
# @deco1
# def func1():
#     print('实现功能1')
# @deco1
# def func2():
#     print('实现功能2')

# fun1 = deco1(func1)
# fun2 = deco1(func2)
# func1()
# func2()

'''
使用装饰器对无参数的函数进行装饰
'''


'''
使用装饰器对有参数的函数进行装饰
'''
#def a(func):
#    print('--1--')
#    def inner(a,b):
#        print('--2--')
#        func(a,b)
#    return inner
#
#@a
#def test(a,b):
#    print("---test-a={},b={}".format(a,b))
#
#test(11,22)

'''
使用装饰器对不定长参数的函数进行装饰
'''
# def a(func):
#     print('----')
#     def inner(*args,**kwargs):
#         print('----')
#         func(*args,**kwargs)
#     return inner
#
# @a
# def test1(a,b,c):
#     print('{},{},{}'.format(a,b,c))
#
# @a
# def test2(a,b,c,d):
#     print('{},{},{},{}'.format(a,b,c,d))
#
# test1(1,2,3)
# test2(11,22,33,44)

'''
使用装饰器对有返回值的函数进行装饰
'''
# def func(functionName):
#     print("---func---1---")
#     def func_in():
#         print("---func_in---1---")
#         ret = functionName()
#         print("---func_in---2---")
#         return ret
#     print("---func---2---")
#     return func_in
#
# def test():
#     print("-----test-----")
#     return "hh"
#
# ret = test()
# print("{}".format(ret))

'''
使用通用装饰器完成对函数进行装饰
'''
# def func(functionName):
#     def func_in(*args,**kwargs):
#         ret = functionName(*args,**kwargs)
#         return ret
#     return func_in
#
# #有返回值的函数
# @func
# def test():
#     print("---test---")
#     return "hello"
#
# #普通没有返回值的函数
# @func
# def test2():
#     print('---test2---')
#
# #带参数的函数
# @func
# def test3(a):
#     print("---test3---{}".format(a))
#
# test()
# test2()
# test3(1)

'''
装饰器带参数
'''
def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---记录日志---{}---".format(arg))
            if arg == "":
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func

#1.先执行func_arg("heihei")函数，这个return结果是func这个函数的引用
#2.得到装饰器@func
#3.使用@func对test进行装饰,即test = func(test)

@func_arg("heihei")
def test():
    print("---test---")

@func_arg("haha")
def test2():
    print("---test2---")


