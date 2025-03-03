def update_version(text: str) -> str:
    n1, n2, n3 = map(int, text.split("."))

    n3 += 1
    if n3 > 9:
        n3 = 0
        n2 += 1
        if n2 > 9:
            n2 = 0
            n1 += 1
            if n1 > 9:
                n1 = 0

    return f"{n1}.{n2}.{n3}"


version = input()

result = update_version(version)
print(result)