class Parent :
    def __init__(self) :
        self.public_var = "Public"
        self._protected_var = "Protected"
        self.__private_var = "Private"
    
    def access_from_same_class(self) :
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

class Child(Parent) :
    def access_from_subclass(self):
        print("Inside child class")
        print(self.public_var)
        print(self._protected_var)
        print(self.__private_var)

p1=Parent()
c1=Child()
p1.access_from_same_class()
c1.access_from_subclass()