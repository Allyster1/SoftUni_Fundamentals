def is_perfect(number: int) -> str:
    dividers_sum = 0

    for divisor in range(1, number):
        if number % divisor == 0:
            dividers_sum += divisor

    if number == dividers_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


input_number = int(input())

result = is_perfect(input_number)

print(result)