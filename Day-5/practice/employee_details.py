class Employee : 
    def __init__(self,name="John",emp_id="123",dept="dev",email="j@gmail.com",phone_number="1234577"):
        self.name =  name 
        self.emp_id = emp_id
        self.dept = dept
        self.email = email
        self.phone_number = phone_number 

    def display(self) :
        print(f"Name  : {self.name} \nEmp ID : {self.emp_id} \nDepartment : {self.dept} \nEmail : {self.email} \nPhone number : {self.phone_number}")
    
    def position(self,*args) :
        if(len(args)==1 and type(args[0]=='str')) :
            print("Position : ", args[0])
        elif len(args)==2 :
            print("Position : ", args[0])
            print("Salary : ", args[1])
    def department(self) :
        print("This is a your department")
        
class Engineer(Employee) :
    def department(self):
        print("Engineering Department")
    def engineer(self) :
        print("I engineer new things")

class Finance(Employee) :
    def department(self):
        print("Finance Department")
    def work(self) :
        print("I deal with numbers")

class Accountant(Finance) :
    def department(self):
        print("Team Accountant")
    def work(self):
        return super().work()

class Auditor(Finance) :
    def work(self) :
        print("I audit numbers")
        
class Finacial_Engineer(Engineer,Finance) :
    def fin(self) :
        print("I deal with fintech")
    
name = input("Enter Name : ")
emp_id = input("Enter your employee id : ")
dept= input("Enter your department : ")
email = input("Enter you email : ")
phone_number = input("enter phone number  : ")

e1=Employee(name=name,emp_id=emp_id,dept=dept,email=email,phone_number=phone_number)
e1.display()
e1.position("analyst")
e1.position("analyst",100000)

for deptartment in [Engineer(),Finance()] :
    deptartment.department()

a1=Accountant()
a1.work()
a1.department()

ad1=Auditor()
ad1.work()

f1=Finacial_Engineer()
f1.engineer()
f1.work()
f1.fin()
f1.department()
Finance.department(f1)
print(f1.__mro__)
