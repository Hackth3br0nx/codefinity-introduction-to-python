# Define inventory
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce"),
}

# Retrieve bread details
bread_details = grocery_inventory["Bread"]
print("Details of Bread:", bread_details)

# Add cookies
grocery_inventory["Cookies"] = (143, "Bakery")
print("Inventory after adding Cookies:", grocery_inventory)

#remove eggs
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)