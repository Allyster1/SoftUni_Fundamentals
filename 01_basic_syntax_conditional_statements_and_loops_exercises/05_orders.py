order_num = int(input())
total = 0

while order_num > 0:
    price = float(input())
    days = int(input())
    amount = int(input())

    order_num -= 1

    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= amount <= 2000:
        print(f"The price for the coffee is: ${price * days * amount:.2f}")
        total += price * days * amount
    else:
        continue

print(f"Total: ${total:.2f}")