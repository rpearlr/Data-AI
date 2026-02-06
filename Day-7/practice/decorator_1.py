def decorator(func) :
    def wrapper(*args,**kwargs):
        print("before")
        print(func(*args,**kwargs))
        print("after")
    return wrapper

@decorator
def add(*args) :
    return sum(args[0])

@decorator
def sub(*args) :
    return args[0]-args[1]

add([3,4,5])
sub(5,4)