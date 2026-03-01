# items discount and stock status have been defined
discounted = False
lowStock = True

# Step 1, combine the conditions to check to see if the item is either discounted or low in stock
movingProduct = discounted or lowStock
# Step 2, use the appropriate operate to check if the item is not eligible for promotion
promotion = not movingProduct

# 3 print the eligibility status 

print("Is the item eligible for promotion?", promotion)