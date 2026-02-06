import access

ch = input("Do you want to register or login  : ")
if ch=="register" :
    user = input("enter your username : ")
    password = input("enter your password : ")
    phone = input("enter your phone : ")
    access.user_register(user,password,phone)
else :
    user = input("enter your username : ")
    password = input("enter your password : ")
    access.user_validate(user,password)