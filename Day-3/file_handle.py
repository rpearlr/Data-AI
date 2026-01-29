file=open("notes.txt","w")
file.write("Welcome to python\n")
file.write("this a sample")
file.close()
# file=open("notes.txt","r")
# content=file.read()
# print(content)
# file.close()
file=open("notes.txt","a")
file.write("\nThis is file handling \n")
file.close()

with open("notes.txt","r") as file  :
  print(file.readline().strip())

with open("notes.txt","r") as file :
  while True:
    line=file.readline()
    if not line:
      break
    print(line.strip())