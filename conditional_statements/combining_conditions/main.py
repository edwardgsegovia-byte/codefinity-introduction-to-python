discounted = True
lowStock = False

movingProduct = discounted or low_stock
promotion = not movingProduct

print("Is the item eligible for promotion?", promotion)