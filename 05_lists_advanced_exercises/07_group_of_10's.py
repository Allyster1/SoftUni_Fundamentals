numbers_list = [int(number) for number in input().split(", ")]
current_group = 10

while numbers_list:
    filtered_numbers = [number for number in numbers_list
                        if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10
    numbers_list = [number for number in numbers_list
                    if number not in filtered_numbers]