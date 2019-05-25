#with与'上下文管理器'

'''
普通版
缺点(Disadvantage):在写的时候容易出现异常导致后面的close函数无法执行
                   很可能导致出现文件无法打开的情况
'''
# def m1():
#     f = open('text.txt','w')
#     f.write('我来说一句')
#     f.close()

'''
进阶版
优点(Advantage):这个是普通版本的升级版，采用了try-except模式，确保最终能够执行close函数
'''
# def m2():
#     f = open('text.txt','w')
#     try:
#         print('writing')
#         f.write('我来说一句进阶版本的')
#         print('write success')
#     except IOError:
#         print('oops error')
#     finally:
#         f.close()
#         print('close success')

'''
高级版
上下文管理器:一个对象实现了__enter__(),__exit__()方法就能称为上下文管理器
特征(Feature):能够使用with关键字
优点(Advantage):简介，优雅，高端大气上档次。
过程(Process):open方法的返回值赋值给变量f,当离开with代码块的时候，系统会自动调用f.close()方法
with的作用和使用try/finally语句是一样的。
'''
# def m3():
#     with open('text.txt','w') as f:
#         f.write("来吧！给你们展示高级用法")

#上下文管理器
class File():

    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('entering')
        self.f = open(self.filename,self.mode)
        return self.f

    def __exit__(self, *args):
        print('will exit')
        self.f.close()

with File('test.txt','w') as f:
    print('writing')
    f.write('hello,Python')
