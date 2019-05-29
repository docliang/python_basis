#coding=utf-8
import time,datetime,threading
#############################################################
#单线程执行
# def saySorry():
#     print('什么时候吃饭？')
#     time.sleep(1)

# def saySorry():
#     print("It's my fault")
#     time.sleep(1)
#
# def multi():
#     starttime = datetime.datetime.now()
#     for i in range(5):
#         try:
#             t = threading.Thread(target=saySorry)
#             t.start()
#         except Exception as e:
#             print('error')
#     endtime = datetime.datetime.now()
#     print('多线程执行时间:{}'.format(endtime-starttime))
#
# def single():
#     starttime = datetime.datetime.now()
#     for i in range(5):
#         try:
#             saySorry()
#         except Exception as e:
#             print('error')
#     endtime = datetime.datetime.now()
#     print('单线程执行时间:{}'.format(endtime-starttime))
#
# if __name__ == '__main__':
#     print('----多线程开始---')
#     multi()
#     print('---单线程开始---')
#     single()
#
#############################################################
#主线程会等待所有的子线程结束后才结束
# def sing():
#     for i in range(3):
#         print('正在唱歌{}'.format(i))
#         time.sleep(1)
#
# def dance():
#     for i in range(3):
#         print('正在跳舞{}'.format(i))
#         time.sleep(1)
#
# if __name__ == '__main__':
#     print('开始：{}'.format(time.ctime()))
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()
#     time.sleep(5)
#     print('结束:{}'.format(time.ctime()))

#############################################################
#查看线程数量
# def sing():
#     for i in range(3):
#         print('正在唱歌{}'.format(i))
#         time.sleep(1.5)
#
# def dance():
#     for i in range(3):
#         print('正在跳舞{}'.format(i))
#         time.sleep(1.5)
#
# if __name__ == '__main__':
#     print('Start:{}'.format(time.ctime()))
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()
#
#     while True:
#         length = len(threading.enumerate())
#         print('the number of threading are {}'.format(length))
#         if length<=1:
#             break
#
#         time.sleep(0.5)

#############################################################
#封装线程
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             msg = "I am "+self.name+'@'+str(i)
#             print(msg)
#
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()
#

#############################################################
#多线程-共享全局变量
#Advantage:在一个进程内所有的线程共享全局变量，方便在多个线程间共享数据
#Disadvantage:线程对全局变量随意篡改可能造成多线程之间对全局变量的混乱,即线程非安全

# g_num = 100
#
# def work1():
#     global g_num
#     for i in range(3):
#         g_num += 1
#     print('---in work1,xxx is {}'.format(g_num))
#
# def work2():
#     global  g_num
#     print('---in work2,xxx is {}'.format(g_num))
#
# print('the xxx which before the threading created is {}'.format(g_num))
#
# t1 = threading.Thread(target=work1)
# t1.start()
# time.sleep(1)
# t2 = threading.Thread(target=work2)
# t2.start()

#############################################################
#列表当作实参传递到线程中
def work1(num):
    num.append(44)
    print('in work1 ',num)

def work2(num):
    time.sleep(1)
    print('in work2 ',num)

g_nums = [11,22,33]

t1 = threading.Thread(target=work1,args=(g_nums,))
t1.start()

t2 = threading.Thread(target=work2,args=(g_nums,))
t2.start()























