def check_capacity(rooms: int):
    total_free_chairs = 0
    chairs_needed = []

    for room in range(1, rooms + 1):
        current_visit = input().split()

        number_of_chairs = len(current_visit[0])
        number_of_visitors = int(current_visit[1])

        if number_of_chairs >= number_of_visitors:
            total_free_chairs += number_of_chairs - number_of_visitors
        else:
            chairs_needed.append((room, number_of_visitors - number_of_chairs))

    if not chairs_needed:
        print(f"Game On, {total_free_chairs} free chairs left")
    else:
        for room, needed in chairs_needed:
            print(f"{needed} more chairs needed in room {room}")


rooms_number = int(input())

check_capacity(rooms_number)
