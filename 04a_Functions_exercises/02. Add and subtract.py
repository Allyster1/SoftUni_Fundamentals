def sum_numbers(first: int, second: int) -> int:
    return first + second


def subtract(result: int, third: int) -> int:
    return result - third


def add_and_subtact(first: int, second: int, third: int) -> int:
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = add_and_subtact(first_number, second_number, third_number)
print(result)
