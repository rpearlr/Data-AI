def power(a,b):
  if b==1:
    return a
  return a * power(a,b-1)

def prime(a,b=2):
  if a==0 or a==1 :
    return False
  if a<=3 :
    return True
  if a%b==0 :
    return False
  if b*b>a:
    return True
  return prime(a,b+1)
  
def calc(a,b):
  op=input("Enter operation: ")
  match op:
    case "+":
      return a+b
    case "-":
      return a-b
    case "*":
      return a*b
    case "/":
      return a/b
    case "%":
      return a%b
    case "//":
      return a//b
    case "^":
      return a^b
    case _:
      return "Not a valid operator"

a= int(input("Enter "))
b= int(input("Enter "))
print(power(a,b))
print(prime(a))
print(calc(a,b))
