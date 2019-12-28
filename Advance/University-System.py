#coding=utf-8
#Time 2019/12/25

class Student():
    def __init__(self,name,sid,password,age,gender):
        '''
        初始化学生属性
        :param name:
        :param sid:
        :param password:
        :param age:
        :param gender:
        '''
        self.name = name
        self.sid = sid
        self.pword = password
        self.age = age
        self.gender = gender

    def findme(self):
        a = 0
        for i in Studentlist:
            if i.sid == self.sid:
                return a
            else:a += 1

    def detail(self):
        print('Your name is {}, age is {},gender is {}'.format(self.name,self.age,self.gender))

    def cancel(self):
        print('Are you sure? Y or N')
        choose = input()
        if choose == 'Y':
            Studentlist.__delitem__(self.findme())
            print('success')
        elif choose == 'N':
            pass
        else:
            print('Error input')


    def menu(self):
        while True:
            print('*******Student Menu*******')
            print('*****0.Cancel account*****')
            print('*****1.Show detail********')
            print('**Press any key to exit!**')
            choose = input()
            if choose == '1':
                self.detail()
            elif choose == '2':
                pass
            elif choose == '0':
                self.cancel()
                break
            else:
                break

class Teacher():
    def __init__(self,name,tid,password,subject,gender):
        '''
        初始化教师属性
        :param name:
        :param tid:
        :param password:
        :param subject:
        :param gender:
        '''
        self.name = name
        self.tid = tid
        self.pword = password
        self.subject = subject
        self.gender = gender

    def findme(self):
        a = 0
        for i in Teacherlist:
            if i.tid == self.tid:
                return a
            else:a += 1


    def detail(self):
        print('name:{},gender:{},subject:{}'.format(self.name,self.gender,self.subject))


    def menu(self):
        while True:
            print('Teacher Menu')
            print('1.Show my detail')
            print('Press any key to exit!')
            choose = input()
            if choose == '1':
                self.detail()
            else:
                break


def register():
    print('1.Student Register')
    print('2.Teacher Register')
    choose = input()
    if choose == '1':
        print('Your name:')
        name = input()
        print('Your gender')
        gender = input()
        print('Your age')
        age = input()
        while True:
            print('Your id')#唯一的id
            id = input()
            flag = 0
            for i in Studentlist:
                if i.sid == id:#如果ID已经存在
                    print('This id was already exist')
                    flag = 1
            if flag == 1:
                continue
            else:break
        print('password')
        password = input()
        stu = Student(name,id,password,age,gender)
        Studentlist.append(stu)
    elif choose == '2':
        print('Your name:')
        name = input()
        print('Your gender')
        gender = input()
        print('subject')
        sub = input()
        while True:
            print('Your id')#唯一的id
            id = input()
            flag = 0
            for i in Teacherlist:
                if i.tid == id:#如果ID已经存在
                    print('This id was already exist')
                    flag = 1
            if flag == 1:
                continue
            else:break
        print('password')
        password = input()
        tec = Teacher(name,id,password,sub,gender)
        Teacherlist.append(tec)
        print('success')

    else:
        pass


def login():
    while True:
        print('1.Student login')
        print('2.Teacher login')
        print('3.Register')
        print('Press any key to exit')
        choose = input()
        if choose == '1':
            print('Please input your id:')
            id = input()
            print('Please input your password:')
            password = input()
            for i in Studentlist:
                if i.sid == id and i.pword == password:
                    print('login success')
                    i.menu()
            else:print('id or password error')
                    # return False

        elif choose == '2':
            print('Please input your id:')
            id = input()
            print('Please input your password:')
            password = input()
            for i in Teacherlist:
                if i.tid == id and i.pword == password:
                    i.menu()
                else:
                    print('id or password error')
                    # return False

        elif choose == '3':
            register()
        else:
            break



if __name__ == '__main__':
    Studentlist = []#学生队列
    Teacherlist = []#教师队列
    a1 = Student('lilin','1','123456',12,'man')
    Studentlist.append(a1)
    login()

