data = input().split()
stock = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantity = data[i + 1]
    stock[product] = int(quantity)

search_products = input().split()

for product in search_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don\'t have {product}")