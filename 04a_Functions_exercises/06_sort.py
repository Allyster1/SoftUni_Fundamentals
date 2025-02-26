
def sort_numbers(numbers_list: list) -> list:
    nums_sorted = sorted(numbers_list)
    return nums_sorted


input_list = input().split()
num_list = []

for i in input_list:
    num_list.append(int(i))

result = sort_numbers(num_list)

print(result)
