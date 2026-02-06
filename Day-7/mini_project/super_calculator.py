import math
def get_numbers() :
     a = int(input("Enter number : "))
     b =  int(input("Enter number : "))
     return a,b

def get_operator() :
    choice = input("1. +\n2. -\n3. *\n4. /\n5. **\n6. //\n7. sqrt\nPlease enter : ")
    return choice

def add(a,b) :
    return a+b   

def sub(a,b) :
    return a-b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

def expo(a,b) :
    return a**b

def floor(a,b) :
    return a//b

def sqrtof(a,b):
    sqrt_a=math.sqrt(a)
    sqrt_b = math.sqrt(b)
    return sqrt_a,sqrt_b