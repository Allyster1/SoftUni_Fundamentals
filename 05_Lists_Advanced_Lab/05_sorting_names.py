def sorting_names(names: list) -> list:
    sorted_names = sorted(names, key=lambda x: (-len(x), x))

    return sorted_names


input_string = input().split(", ")

result = sorting_names(input_string)
print(result)