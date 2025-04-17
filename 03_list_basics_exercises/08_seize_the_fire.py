level_of_fire = input().split("#")
water = int(input())

cells = []
effort = 0
total_fire = 0

for i in level_of_fire:
    line = i.split(' = ')

    fire_type = line[0]
    cell_value = int(line[1])

    valid = False
    if fire_type == "High" and 81 <= cell_value <= 125:
        valid = True
    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        valid = True
    elif fire_type == "Low" and 1 <= cell_value <= 50:
        valid = True

    if valid and water >= cell_value:
        cells.append(cell_value)
        water -= cell_value
        effort += cell_value * 0.25
        total_fire += cell_value

print("Cells:")
for i in cells:
    print(f" - {i}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")