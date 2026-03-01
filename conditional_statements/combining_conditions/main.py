# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Step 1: Combine the conditions to check if the item is either discounted or low in stock
movingProduct = discounted or lowStock

# Step 2: Use the appropriate operator to check if the item is not eligible for promotion
promotion = not movingProduct

# Step 3: Print the eligibility status
print("Is the item eligible for promotion?", promotion)