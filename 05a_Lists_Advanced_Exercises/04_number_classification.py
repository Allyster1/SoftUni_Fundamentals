def positive_numbers(list_of_numbers: list) -> str:
    return ", ".join([num for num in list_of_numbers if int(num) >= 0])


def negative_numbers(list_of_numbers: list) -> str:
    return ", ".join([num for num in list_of_numbers if int(num) < 0])


def even_numbers(list_of_numbers: list) -> str:
    return ", ".join([num for num in list_of_numbers if int(num) % 2 == 0])


def odd_numbers(list_of_numbers: list) -> str:
    return ", ".join([num for num in list_of_numbers if int(num) % 2 != 0])


numbers = input().split(", ")

print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")
