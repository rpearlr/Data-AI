import datetime
import re
errors = []
with open("sample_logs.log","r") as log : 
  lines = log.readlines()
  for line in lines :
    if re.search("WARN",line) or re.search("ERROR",line) :
      errors.append(line)

formatted="".join(str(datetime.date.today()))
newpath = rf"C:\Users\User\Desktop\logs_{formatted}.txt"
with open(newpath,"w") as f :
  for err in errors :
    f.write(err)