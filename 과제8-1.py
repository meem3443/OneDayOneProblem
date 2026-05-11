
class Person:
    def __init__(self, n, m = "010-0000-0000", o = "02-0000-0000", e = "example@gmail.com"):
        self.n = n
        self.m = m
        self.o = o
        self.e = e

    def  __str__(self):
        return f"이름 : {self.n} \n핸드폰 : {self.m} \n직장전화 : {self.o} \n이메일 : {self.e}"

    def setName(self, n):
        self.n = n

    def getName(self):
        return self.n

    def setMobile(self, m):
        self.m = m

    def getMobile(self):
        return self.m

    def setOffice(self, o):
        self.o = o

    def getOffice(self):
        return self.o

    def setEmail(self, e):
        self.e = e

    def getEmail(self):
        return self.e

p1 = Person("홍길동")
print(p1)
print()
p1.setMobile("010-1234-5678")
print(p1)


