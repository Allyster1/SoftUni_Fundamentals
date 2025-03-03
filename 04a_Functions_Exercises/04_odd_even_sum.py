def even_odd_sum(number: str) -> str:
    even_sum = 0
    odd_sum = 0

    for num_char in number:
        if num_char % 2 == 0:
            even_sum += int(num_char)
        elif num_char % 2 != 0:
            odd_sum += int(num_char)

    res = f"Odd sum = {odd_sum}, Even sum = {even_sum}"

    return res


number_input = input()

result = even_odd_sum(num)
print(result)