seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# define overstock risk
overstock_risk = seasonal and (current_stock > high_stock_threshold)
discount_eligible = (not selling_well and not on_sale)
make_discount = discount_eligible or overstock_risk

# print
print("Should the item be discounted?", make_discount)