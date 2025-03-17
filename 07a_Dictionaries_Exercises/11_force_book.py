force_data = {}

while True:
    line = input()

    if line == "Lumpawaroo":
        break

    if " | " in line:
        side, user = line.split(" | ")
        user_exists = any(user in users for users in force_data.values())

        if not user_exists:
            if side not in force_data:
                force_data[side] = []
            force_data[side].append(user)

    elif " -> " in line:
        user, side = line.split(" -> ")
        user_exists = False
        current_side = None

        for existing_side, users in force_data.items():
            if user in users:
                user_exists = True
                current_side = existing_side
                break

        if user_exists:
            force_data[current_side].remove(user)

        if side not in force_data:
            force_data[side] = []
        force_data[side].append(user)

        print(f"{user} joins the {side} side!")

for side, users in force_data.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")