import datetime
errors = []
with open("sample_logs.log","r") as log : 
  lines = log.readlines()
  for line in lines :
    content = line.split(" ")
    if(content[2]=="WARN" or content[2]=="ERROR") :
      errors.append(line)

formatted="".join(str(datetime.date.today()))
newpath = rf"C:\Users\User\Desktop\logs_{formatted}.txt"
with open(newpath,"w") as f :
  for err in errors :
    f.write(err)