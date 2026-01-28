import shutil

def get_items():
  items={}
  while True :
    item=input("enter the name of the item : ")
    amount=int(input("enter the amount of the item : "))
    items[item] = amount
    done=input("are you done : ")
    if done == "y":
      break
  return items 

def profile(**kwargs):
  dict={}
  for key,value in kwargs.items():
    dict[key.upper()] =  value.strip()
  return dict

def print_user(*args) :
  dict=args[0]
  print(dict)
  mask=dict["PHONE"][:2] + "*" * 6 + dict["PHONE"][-2:]
  print(f"{dict["NAME"].title()} is in {dict["LOCATION"].title()} and went to {dict["RESTAURENT_NAME"].title()}. The phone number is {mask}")

def print_final_bill(*args):
  dict = args[0]
  sum=0
  for key,value in dict.items() :
    print(f"Item : {key.strip().title()}      Price : {value}")
    sum=sum+value
  
  print(f"Your final total bill is {sum}")

def get_user_details():
  name =input("enter your name : ")
  phone = input("enter your phone number : ")
  location = input("enter your location : ")
  restaurent_name=input("enter the restaurent : ")
  dict=profile(name=name,phone=phone,location=location,restaurent_name=restaurent_name)
  return dict

def download_bill(*args):
  dict=args[0]
  path=r"C:\Users\User\Desktop\bill.txt"
  with open(path, "a") as f:
      for key,value in dict.items() :
        f.write(f"Item : {key.strip().title()}      Price : {value}\n")
  print(f"the bill has been downloaded at {path}")
  return path

def make_copy_bill(path) :
  newpath = r"C:\Users\User\Desktop\bill2.txt"
  shutil.copy(path,newpath)

