#闭包介绍
#def test(number):
#    print('---1---')
#
#    def test_in(number2):
#        print('---2---')
#        print(number + number2)
#
#    print('---3---')
#    return test_in
#
#
#ret = test(100)
#print('-'*7)
#ret(1)

#闭包实例
#def line_conf(a,b):
#    def line(x):
#        return a*x + b
#
#    return line
#
#line1 = line_conf(1,1)
#line2 = line_conf(4,5)
#print(line1)
#print(line2)
#print(line1(5))
#print(line2(5))

def createNum(a,b,x):
    print(a*x+b)

a = 1
b = 1
x = 0
createNum(a,b,x)