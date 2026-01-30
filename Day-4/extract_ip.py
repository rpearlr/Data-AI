ip_address=[]
with open("sample_logs.log","r") as log :
 lines= log.readlines()
 for line in lines :
  word = line.split("[")
  ip_addr = word[1].split("]")
  print(ip_addr)
  ip_address.append(ip_addr[0])

with open("ip_addr.txt","w") as ip :
 for addr in ip_address:
  ip.write(addr + "\n")
