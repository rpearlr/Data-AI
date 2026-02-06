def user_valid(func):
    def wrapper(user,password) :
        if user == "admin" and  password == "1234" :
            return func(user,password)
        else :
            print("Invalid")
    return wrapper

@user_valid
def view_dashboard(user,password) :
    print("You can view dashboard")

view_dashboard("admin","12354")