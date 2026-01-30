try:
    items = {"apple":30,"grapes":60,"guava":45,"strawberry":100}
    total_cost = 0
    while True :
        item = input("Enter the name of the item : ")
        if item not in items :
            raise Exception('Item is not availble at Zomato')
        quantity = int(input("Enter quantity per item : "))
        if quantity <=0 :
            raise Exception("Quantity cannot be less than 1")
        total_cost = total_cost + items[item] * quantity
        choice = input("Are you done : ")
        if choice == 'yes' :
            break
    print("The final cost is : ", total_cost)
except ValueError as e :
    print("Please enter the right value : ",e)
except Exception as e :
    print("An exception has occured : ",e)
finally :
    print("Thank you for shopping at Zomato")

