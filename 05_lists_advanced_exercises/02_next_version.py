def update_version(text: str) -> str:
    third, second, first = map(int, text.split("."))

    first += 1
    if first > 9:
        first = 0
        second += 1
        if second > 9:
            second = 0
            third += 1

    return f"{third}.{second}.{first}"


version = input()

result = update_version(version)
print(result)