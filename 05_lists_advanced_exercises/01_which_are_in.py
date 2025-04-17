def find_substring(first: list, second: str) -> list:
    sequence = []

    for substring in first:
        if substring in second and substring not in sequence:
            sequence.append(substring)

    return substr_sequence


first_sequence = input().split(", ")
second_sequence = input()

result = find_substring(first_sequence, second_sequence)
print(result)