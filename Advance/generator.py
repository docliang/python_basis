#coding=utf-8
# #list
# a = [i for i in range(10)]
#生成器介绍：在迭代器的基础之上，不用我们人工记录当前迭代状态，简而言之就是省事
# #第一种创建generator,生成器占用内存较少
# b = (i for i in range(10))
#
# c = [{'name':'wang','age':22},{'name':'li','age':33}]
#
# d = {'score':[1,2,3,4,5],'city':['成都','北京','南阳']}

# #next
# def createNum():
#     print('---start---')
#     a,b = 0,1
#     for i in range(5):
#         print('---1---')
#         yield b
#         print('---2---')
#         a,b = b,a+b
#         print('---3---')
#     print('---stop---')
#
# #send
# def test():
#     i = 0
#     while i<5:
#         temp = yield i
#         print(temp)
#         i += 1


#第二种实现生成器的方法
#在使用生成器实现的方式中，我们将原本在迭代器__next__方法中实现的基本逻辑放到一个函数中来实现，但是将每次迭代返回数值的return换成了yield
#此时新定义的函数便不再是函数，而是一个生成器了。简单来说:只要在def中有yield关键字的就称为生成器
#
# def fib(n):
#     current = 0
#     num1,num2 = 0,1
#     while current < n:
#         num = num1
#         num1,num2 = num2,num1+num2
#         current += 1
#         yield num
#     return 'ok'
#
# f = fib(5)
# while True:
#     try:
#         x = next(f)
#         print(x)
#     except StopIteration as e:
#         print('The return value of generator is {}'.format(e.value))
#         break

#使用for循环调用generator时，发现拿不到generator的return语句的返回值。若想拿到返回值必须捕获StopIteration错误，返回值包含在它的value中


###############################################################################################################
#Summary:
#1.使用了yield关键字的函数不再是函数，而是生成器。
#2.yield关键字有两点作用：
#    保存当前运行状态(断点)，然后暂停执行，即将生成器(函数)挂起
#    将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
#3.可以使用next()函数让生成器从断点处继续执行，即唤醒生成器(函数)
#4.Python3中的生成器可以使用return返回最终运行的返回值，而Python2中的生成器不允许使用return返回一个返回值

###############################################################################################################

#使用send唤醒
#除了使用next()函数来唤醒生成器继续执行外，还可以使用send()函数来唤醒执行。使用send()函数的一个好处是可以在唤醒的同时向断点处传入一个附加数据

def gen():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i += 1

