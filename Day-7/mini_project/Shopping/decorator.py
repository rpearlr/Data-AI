def user_valid(func):
    def wrapper(user,password) :
        if user == "admin" and  password == "1234" :
            return func(user,password)
        else :
            print("Invalid")
    return wrapper