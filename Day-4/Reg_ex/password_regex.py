import re
password = input("please enter your passoword ")

checks=[False,False,False,False,False]
if re.search(r'[A-Z]',password) :
  checks[0]=True
if re.search(r'[a-z]',password) :
  checks[1]=True
if re.search(r'[0-9]',password) :
  checks[2]=True 
if re.search(r'[^a-zA-Z0-9_]', password):
  checks[3]=True
if len(password) >= 8 :
  checks[4]=True
print(checks)
if not False in checks :
  print("The password is strong")
