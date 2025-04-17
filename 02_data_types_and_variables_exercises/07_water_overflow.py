fillings_count = int(input())
water_tank = 0

for i in range(fillings_count):
    liters = int(input())

    if water_tank + liters > 255:
        print("Insufficient capacity!")
        continue
    else:
        water_tank += liters

print(water_tank)