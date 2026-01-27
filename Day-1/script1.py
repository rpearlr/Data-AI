import sys
print(len(sys.argv))
if len(sys.argv) < 4 :
  sys.exit()
var=sys.argv[1]
print(f"Hello {var}")
for i in range(len(sys.argv)):
  print(f"arg {i} : {sys.argv[i]}")