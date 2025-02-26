def is_even(current_number: int) -> bool:

    return current_number % 2 == 0


input_number = input().split()
num_list = list(map(int, input_number))

filtered_list = list(filter(is_even, num_list))

print(filtered_list)