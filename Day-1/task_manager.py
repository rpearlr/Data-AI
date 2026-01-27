while True :
  choice = int(input("Enter 1.write file 2. read file"))
  match choice :
    case 1 :
      with open(r"C:\Users\User\Desktop\txt5.txt", "a") as f:
        f.write("hellow world")
    case 2 :
      with open(r"C:\Users\User\Desktop\txt5.txt", "r") as f:
        print(f.read())
