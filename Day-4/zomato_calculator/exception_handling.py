try :
    a=int(input("Enter number 1 : "))
    b=int(input("Enter number 2 : "))
    result = a/b
    print("Result is ",result)
except Exception as e :
    print("Error is : ", e)
finally :
    print("It is done")