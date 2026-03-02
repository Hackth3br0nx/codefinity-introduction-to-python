vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
Vegetable_Inventory = vegetables


if "carrots" not in vegetables:
    vegetables.append("carrots")

else:
    print("Carrots are already in the list")
    
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")

else:
    print("Cucumbers are already in the list")
    
vegetables.sort()
print("Updated Vegetable Inventory:", Vegetable_Inventory)

