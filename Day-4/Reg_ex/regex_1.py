import re
text="python is powerful"
res = re.search("python",text)
if res :
  print("Match found", res.group())

text1 = "my number is 1234567890 and 9867543210"
num = re.findall("\d{10}",text1)
print(num)

for match in re.finditer("\d{10}",text1):
  print("MAtch from",match.start(),"to",match.end())

text2="my phone is 1234567890"
masked = re.sub(R'\d','*',text2)
print(masked)