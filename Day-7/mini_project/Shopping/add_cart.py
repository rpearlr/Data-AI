def addcart() : 
    items = {"apple":30,"grapes":60,"guava":45,"strawberry":100}
    total_cost = 0
    cart = {}
    while True :
            item = input("Enter the name of the item : ")
            quantity = int(input("Enter quantity per item : "))
            cart[item] = quantity
            total_cost = total_cost + items[item] * quantity
            choice = input("Are you done : ")
            if choice == 'yes' :
                break
