items_input = input().split('|')
budget = float(input())

bought_items = []
max_prices = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}

for item in items_input:
    item_type, price_str = item.split('->')
    price = float(price_str)
    if item_type in max_prices and price <= max_prices[item_type]:
        if budget >= price:
            budget -= price
            bought_items.append(price)

new_prices = [price * 1.40 for price in bought_items]
profit = sum(new_prices) - sum(bought_items)

print(' '.join([f'{price:.2f}' for price in new_prices]))
print(f'Profit: {profit:.2f}')

total_money = budget + sum(new_prices)
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")