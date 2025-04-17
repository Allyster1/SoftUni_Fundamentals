list_of_strings = input().split()
counter = int(input())

list_of_numbers = [int(number) for number in list_of_strings]

for i in range(counter):
    smallest_int = min(list_of_numbers)

    list_of_numbers.remove(smallest_int)

result = ', '.join(str(number) for number in list_of_numbers)

print(result)