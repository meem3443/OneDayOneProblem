class Cat:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
    def __str__(self):
        return f"고양이 이름: {self.name}, 나이: {self.age}"
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age
        
cat1 = Cat("나비", 3)
cat2 = Cat("보리", 7)
print(cat1)
print(cat2)
