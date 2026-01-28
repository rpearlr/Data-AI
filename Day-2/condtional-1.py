# if bill > 1000 and weekend and gold member give 20% discount

bill = int(input("enter the bill  : "))
day = input("enter the day : ")
membership = input("enter status : ")
weekend=["sat","sun"]
if bill >1000 and day in weekend and membership=="gold":
  print(f"your bill is {bill*0.8}")