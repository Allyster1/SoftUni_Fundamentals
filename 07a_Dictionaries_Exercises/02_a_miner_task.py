resources_dict = {}

while True:
    resource = input()

    if resource == "stop":
        break

    quantity = int(input())

    if resource not in resources_dict:
        resources_dict[resource] = quantity
    else:
        resources_dict[resource] += quantity

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
