import os
def ping_server(hostname) :
  param = '-n' 
  response = os.system(f"ping {param} 1 {hostname}")
  if response == 0:
    print(f"{hostname} is up")
  else:
    print(f"{hostname} is down")

with open("server.txt","r") as f:
  lines = f.readlines()
  for line in lines :
    ping_server(line)

