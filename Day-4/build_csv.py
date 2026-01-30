ip_addr=[]
with open("ip_addr.txt","r") as ip :
  lines = ip.readlines()
  for line in lines :
    ip_addr.append(line)

with open("build.csv","w") as f :
  for ip in ip_addr:
    f.write(ip)
