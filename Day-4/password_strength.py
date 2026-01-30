password = input("please enter your passoword ")
num="1234567890"
special_chars="!@#$%^&*"
checks=[False,False,False,False,False]
for ch in password :
  if ch in num :
    checks[0]=True
  if ch in special_chars :
    checks[1]=True
  if ch.isupper() :
    checks[2]=True 

result_2 = any(c.islower() for c in password)
if result_2 :
  checks[3]=True
if len(password) >= 8 :
  checks[4]=True
print(checks)
if not False in checks :
  print("The password is strong")