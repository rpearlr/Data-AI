def registration(func):
    def wrapper(*args) :
        if not args[0] == None and len(args[1]) > 8 and not args[2] == None :
            return func(args)
        else :
            print("Invalid values are used")
    return wrapper

@registration
def user_registar(*args) :
    print("Valid credentials")

user_registar("Rhea","234567890","9089844469")