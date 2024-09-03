
quantity = int(input("Enter the quantity purchased: "))  

if quantity<100:
    price = 2.50
else:
    price = 1.75
total_cost = quantity * price

print("Your total cost for", quantity, "items at", price, "per item is", total_cost, ".")
