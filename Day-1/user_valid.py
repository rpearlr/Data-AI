email = input("Enter email ID : ")
password = input("Enter password : ")
ia=False
b=False
if "@" in email and ".com" in email:
  a=True
if len(password)>=8:
  b= True
if a and b:
  print("valid username and password")
elif a:
  print("password is invalid")
elif b:
  print("username is invalid")
else :
  print("username and passowrd are invalid")

name = input("enter name : ")
age =(input("enter age : "))
if name.isalpha() :
  print("name is valid")
if age.isdigit() :
  print("age is valid")