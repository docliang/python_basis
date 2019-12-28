class people():
    def __init__(self,name,id):
        self.name = name
        self.id = id

if __name__ == '__main__':
    Peo = []
    a1 = people('lilin',1)
    a2 = people('wanglin',2)
    Peo.append(a1)
    Peo.append(a2)
    for i in Peo:
        print(i)
    Peo.remove(i.id)
    print(Peo)