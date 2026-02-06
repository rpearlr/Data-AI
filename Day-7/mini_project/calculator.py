import super_calculator

a,b=super_calculator.get_numbers()
ch=super_calculator.get_operator()
match ch :
    case "+":
      print( super_calculator.add(a,b) )
    case "-":
      print( super_calculator.sub(a,b) )
    case "*":
      print( super_calculator.mul(a,b) )
    case "/":
      print( super_calculator.div(a,b) )
    case "**":
      print( super_calculator.expo(a,b) )
    case "//":
      print( super_calculator.floor(a,b) )
    case "sqrt" :
        print( super_calculator.sqrtof(a,b) )
    case _:
        print("Not applicable" )