def profile(**kwargs):
  dict={}
  for key,value in kwargs.items():
    dict[key.upper()] =  value.strip()
  return dict


name = input("enter name : ")
age = input("enter age : ")
email = input("enter your email : ")
location = input("enter you location : ")

dict = print(profile(name=name,age=age,email=email,location=location))
