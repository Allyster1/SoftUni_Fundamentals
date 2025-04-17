while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    text = ""
    for i in command:
        text += i + i
    print(text)