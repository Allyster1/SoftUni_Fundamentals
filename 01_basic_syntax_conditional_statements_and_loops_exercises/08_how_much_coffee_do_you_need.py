counter = 0
flag = False

while True:
    command = input()

    if command == "END":
        break

    text = command.lower()

    if text == "dog" or text == "cat" or text == "coding" or text == "movie":
        if command.isupper():
            counter += 2
        else:
            counter += 1
    else:
        continue

    if counter > 5:
        print("You need extra sleep")
        flag = True

if flag is False:
    print(counter)