# Define lists
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustaaaaaaaaaaaaard", 1.99, 75, "Spicy"]

# Define Main list
deli_dept = [meat, cheese, condiment]
print(f"Initial Deli List: {deli_dept}")


# Restock items
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100

# add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)



# remove condiment
deli_dept.remove(condiment)
deli_dept.sort()

print(f"Updated Deli List: {deli_dept}")