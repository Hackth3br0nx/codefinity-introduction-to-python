#Define dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8), 
    "Eggs": ("Dairy", 5.50, 3),
    "Bread": ("Bakery", 2.00, 15),
    "Apples": ("Produce", 1.50, 50)
}

#Check and Update prices
price_of_eggs = grocery_inventory["Eggs"][1]
if price_of_eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, _, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, price_of_eggs - 1, stock)

else:
    print("The price of Eggs is reasonable")

#Add new item
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

#check milk
stock = grocery_inventory["Milk"][2]
if stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_stock = stock + 20
    cat, price, _ = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (cat, price, new_stock)

else: 
    print("Milk has sufficient stock.")

# remove apples
apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)