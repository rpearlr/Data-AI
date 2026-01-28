n= int(input("enter size : "))
for i in range(n):
  for j in range(n):
    if j<=i:
      print("*", end=" ")
    else : 
      print("0",end=" ")
  print()