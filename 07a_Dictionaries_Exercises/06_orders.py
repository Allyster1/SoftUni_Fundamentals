has_bought = False
products_dict = {}

while not has_bought:
    command = input()

    if command == "buy":
        has_bought = True
        break

    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product in products_dict:
        products_dict[product]["quantity"] += quantity
        if products_dict[product]["price"] != price:
            products_dict[product]["price"] = price
    else:
        products_dict[product] = {
            "price": price,
            "quantity": quantity
        }

for product, details in products_dict.items():
    total_price = details["price"] * details["quantity"]
    print(f"{product} -> {total_price:.2f}")