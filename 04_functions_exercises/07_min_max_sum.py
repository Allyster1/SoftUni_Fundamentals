

input_list = input().split()
numbers_list = []

for i in input_list:
    numbers_list.append(int(i))

min_num = min(num_list)
max_num = max(num_list)
total_sum = sum(num_list)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {total_sum}")