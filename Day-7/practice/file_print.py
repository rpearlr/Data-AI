import employee_read
path=input("enter path")
words = employee_read.read_file(path)
print("ID : ", words[0])
print("Name : ", words[1])
print("Salary : ", words[2])
print("Designation : ", words[3])
print("Experiance : ", words[4], "\n")