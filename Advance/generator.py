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

#next
def createNum():
    print('---start---')
    a,b = 0,1
    for i in range(5):
        print('---1---')
        yield b
        print('---2---')
        a,b = b,a+b
        print('---3---')
    print('---stop---')

#send
def test():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i += 1
