def character_multiplier(first: str, second: str):
    total_sum = 0
    min_length = min(len(first), len(second))

    for i in range(min_length):
        total_sum += ord(str1[i]) * ord(str2[i])

    if len(str1) > len(str2):
        for i in range(min_length, len(str1)):
            total_sum += ord(str1[i])
    else:
        for i in range(min_length, len(str2)):
            total_sum += ord(str2[i])

    return total_sum


input_string = input().split()
str1 = input_string[0]
str2 = input_string[1]

result = character_multiplier(str1, str2)
print(result)