parking_dict = {}
parking_capacity = int(input())

for _ in range(parking_capacity):
    parking_command = input().split()
    if parking_command[0] == "register":
        command, name, car_id = parking_command

        if name not in parking_dict:
            parking_dict[name] = car_id
            print(f"{name} registered {car_id} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_id}")
    elif parking_command[0] == "unregister":
        command, name = parking_command

        if name not in parking_dict:
            print(f"ERROR: user {name} not found")
        else:
            parking_dict.pop(name)
            print(f"{name} unregistered successfully")

for name, car_id in parking_dict.items():
    print(f"{name} => {car_id}")