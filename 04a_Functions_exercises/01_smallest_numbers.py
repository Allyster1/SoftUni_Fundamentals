def find_smallest_num(numbers: list) -> int:
    return min(numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())

smallest_num = find_smallest_num([first_number,second_number,third_number])
print(smallest_num)