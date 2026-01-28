for i in range(5):
  if(i==4):
    print("all attempts done")
    break
  user=input("enter username :")
  password=input("enter password : ")
  if user == "admin" and password=="12345":
    print("it is correct")
  else  :
    print(f"you have {3-i} attempts left")
