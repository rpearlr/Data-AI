def add(a,b) :
    return a+b

def sub(a,b) :
    return a-b

def multiply(a,b) :
    return a*b

def divide(a,b) :
    if b == 0 :
        raise ValueError("Cannot divide by 0")
    return a/b

class calcc : 
    def add(self,a,b) :
        return a+b