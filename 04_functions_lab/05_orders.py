def calculate_price(products, counter):
    if products == "coffee":
       return counter * 1.50
    elif products == "water":
        return counter * 1.00
    elif products == "coke":
        return counter * 1.40
    elif products == "snacks":
        return counter * 2.00

product = input()
count = int(input())

result = calculate_price(product, count)

print(f"{result:.2f}")