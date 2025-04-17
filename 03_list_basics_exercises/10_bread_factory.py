events = input().split("|")
total_energy = 100
total_coins = 100
is_open = True

for event in events:
    e_item = event.split("-")
    e_type, e_val = e_item[0], int(e_item[1])

    if e_type == "rest":
        initial_energy = total_energy
        total_energy += e_val

        if total_energy > 100:
            total_energy = 100

        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif e_type == "order":
        if total_energy >= 30:
            total_coins += e_val
            total_energy -= 30
            print(f"You earned {e_val} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= e_val:
            total_coins -= e_val
            print(f"You bought {e_type}.")
        else:
            is_open = False
            break

if is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {e_type}.")
