input_strings = input().split()
total_sum = 0

for current in input_strings:
    front_letter = current[0]
    last_letter = current[-1]

    current_num = int(current[1:len(current) - 1])

    if front_letter.isupper():
        front_letter_position = ord(front_letter) - 64
        total_sum += current_num / front_letter_position
    elif front_letter.islower():
        front_letter_position = ord(front_letter) - 96
        total_sum += current_num * front_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")
