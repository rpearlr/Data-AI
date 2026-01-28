def  add_all(*args):
  sum=0
  for num in args:
    sum+=num
  return sum

print(add_all([1,2,3,4]))

def print_data(**kwargs):
  for key,value in kwargs.items():
    print(f"{key} : {value}")

print_data(name="rhea",age=21)