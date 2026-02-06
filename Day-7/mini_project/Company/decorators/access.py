def user_valid(func):
    def wrapper(user,password) :
        if user == "admin" and  password == "1234" :
            return func(user,password)
        else :
            print("Invalid")
    return wrapper

def registration(func):
    def wrapper(*args) :
        if not args[0] == None and len(args[1]) > 8 and not args[2] == None :
            return func(args)
        else :
            print("Invalid values are used")
    return wrapper