from collections.abc import Iterator,Iterable

#############################################################
#所有的变量都可以理解是内存中一个对象的"引用"
#Iterator && Iterable
#可迭代对象，简单来说就是能够用for循环进行遍历的对象,如python自带的数据类型list,tuple,str,dict
# isinstance([],Iterable)#True
# isinstance({},Iterable)#True
# isinstance((),Iterable)#True
# isinstance('abc',Iterable)#True


#############################################################
#可迭代对象的本质：可迭代对象通过__iter__方法向我们提供一个迭代器，迭代时先获取对象提供的迭代器，通过迭代器迭代
# 一个具备了__iter__方法的对象，就是一个可迭代对象
# class MyList(object):
#     def __init__(self):
#         self.container = []
#
#     def add(self,item):
#         self.container.append(item)
#
#     def __iter__(self):
#         #返回一个迭代器
#         #暂时忽略如何构造一个迭代器对象
#         pass
#
# mylist = MyList()
# isinstance(mylist,Iterable)#True


#############################################################
#iter()函数与next()函数
#如list,tuple这些都是可迭代对象，通过使用iter()函数来获取这些可迭代对象的迭代器，通过next方法获取下一条数据
#iter()函数实际上就是调用了可迭代对象的__iter__方法
# li = [11,22,33,44]#iterable
# # li_iter = iter(li)#iterator
# # next(li_iter)
# # isinstance(li_iter,Iterator)


#############################################################
#迭代器：用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数时，迭代器会向我们返回它所记录位置的下一个位置的数据
#构造一个迭代器:迭代器需要__iter__和__next__两个方法,迭代器本身也能够迭代，因此__iter__方法返回迭代器本身
#总而言之，一个实现了__iter__方法和__next__方法的对象，就是迭代器
#将类的实例变成一个迭代对象

# class MyList(object):
#     #自定义一个可迭代对象
#     def __init__(self):
#         self.items = []
#
#     def add(self,val):
#         self.items.append(val)
#
#     def __iter__(self):
#         myiterator = MyIterator(self) #用自己实例化一个迭代器对象，把自己当参数传进去
#         return myiterator #返回一个迭代器对象
#
#
# class MyIterator(object):
#     #自定义的供上面可迭代对象使用的一个迭代器
#     def __init__(self,mylist):#mylist就是之前实例化传进来的对象
#         self.mylist = mylist
#         #current用来记录当前访问到的位置
#         self.current = 0
#
#     def __next__(self):
#         if self.current < len(self.mylist.items):
#             item = self.mylist.items[self.current]
#             self.current += 1
#             return item
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self
#
#
# if __name__ == '__main__':
#     mylist = MyList()#实例化一个可迭代对象
#     mylist.add(1)
#     mylist.add(2)
#     isinstance(mylist,Iterable)#True


#############################################################
# for item in Iterable 本质：通过iter()函数获得可迭代对象iterable的iterator，
# 然后对获取到的迭代器不断调用next()方法获取下一个值并赋值给item,遇到StopIteration的异常后循环结束


#############################################################
#迭代器应用场景：可以通过一个表达式来推算下一个item，不用固定的数据集合，节省内存，有种数列的feel。
#实例：用迭代器实现斐波那契数列 0,1,1,2,3,5,8.....

class FibIterator(object):
    #斐波那契数列迭代器
    def __init__(self,n):
        '''

        :param n:int,指明生成数列前n个数
        '''
        self.n = n
        #current用来保存当前
        self.current = 0
        #num1用来保存前前一个数，初始值为数列中的第一个数0
        self.num1 = 0
        #num2用来保存前一个数，初始值为数列中的第二个数1
        self.num2 = 1

    def __next__(self):
        #被next()函数调用来获取下一个数
        if self.current < self.n:
            num = self.num1
            self.num1,self.num2 = self.num2,self.num1+self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        #迭代器的__iter__返回自身即可
        return self

# if __name__ == '__main__':
#     fib = FibIterator(10)
#     for num in fib:
#         print(num,end=' ')


#############################################################
#除了for循环能够接收可迭代对象，list,tuple等也能接收
li = list(FibIterator(15))
print(li)
tp = tuple(FibIterator(6))
print(tp)



