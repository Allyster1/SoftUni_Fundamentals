import re
has_bought = False
products = []
total_spent = 0

pattern = r">>(?P<product>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)"

while has_bought is False:
    text = input()

    if text == "Purchase":
        has_bought = True
        break

    match = re.search(pattern, text)
    if match:
        products.append(match.group('product'))
        cost = float(match.group('price')) * int(match.group('quantity'))
        total_spent += cost

print("Bought furniture: ")
for product in products:
    print(product)
print(f"Total money spend: {total_spent:.2f}")

