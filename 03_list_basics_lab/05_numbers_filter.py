n = int(input())

numbers_list = []
filtered_numbers_list = []

for _ in range(n):
    current_num = int(input())
    numbers_list.append(current_num)

command = input()

if command == "even":
    for num in numbers_list:
        if num % 2 == 0:
            filtered_numbers_list.append(num)
elif command == "odd":
    for num in numbers_list:
        if num % 2 != 0:
            filtered_numbers_list.append(num)
elif command == "negative":
    for num in numbers_list:
        if num < 0:
            filtered_numbers_list.append(num)
elif command == "positive":
    for num in numbers_list:
        if num >= 0:
            filtered_numbers_list.append(num)

print(filtered_numbers_list)