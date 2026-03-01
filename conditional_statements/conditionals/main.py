# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

# Input conditional statements
if product_type == "Fruits" and day_of_week == "Monday":
    print("10% discount on Fruits today!")
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print("15% discount on Vegetables today!")
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print("20% discount on Dairy today!")
elif product_type == "Other":
    print("No discount available.")
else:
    print("No special discounts today.")