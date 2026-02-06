class Student :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self) :
        print(f"Hello {self.name}, I'm {self.age} years old ")

s1 = Student(name = "John", age = 22)
s2 = Student(name = "Rhea", age = 21)
s1.hello()
s2.hello()