is_finished = False
gifts_list = input().split()

while not is_finished:
    line = input()

    if line == "No Money":
        is_finished = True
        break

    command = line.split()

    if command[0] == "OutOfStock":
        gift = command[1]
        gifts_list = ["None" if x == gift else x for x in gifts_list]

    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = gift

    elif command[0] == "JustInCase":
        gift = command[1]
        if gifts_list:
            gifts_list[-1] = gift

final_gifts = [gift for gift in gifts_list if gift != "None"]
print(" ".join(final_gifts))