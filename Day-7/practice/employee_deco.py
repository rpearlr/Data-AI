def designation(func) :
    def wrapper(self,des,sal) :
         print( self.des)
         return  func(self,des,sal)
    return wrapper

def salary(func) :
    def wrapper(self,des,sal) :
        print( self.sal)
        return func(self,des,sal)
    return wrapper
class Employee :
    def __init__(self,des,sal):
        self.sal = sal
        self.des = des

    @designation
    @salary
    def display(self,des,sal) :
        print()
    
e1=Employee("Manager",100000)
e1.display("Manager",100000)

