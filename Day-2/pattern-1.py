n= int(input("enter size of rectangle : "))
for i in range(n):
  for j in range(n-i):
    print(" ",end=" ")
  for j in range(i+1) :
    print(f"{i+1} ", end = " ")
  for j in range(n-i):
    print(" ", end =" ")
  print()