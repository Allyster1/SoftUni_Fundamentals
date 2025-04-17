input_string = input().split(", ")

numbers_list = list(map(int, input_string))

even_indexes = [index for index, num in enumerate(numbers_list) if num % 2 == 0]

print(even_indexes)