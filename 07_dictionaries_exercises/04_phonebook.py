phonebook = {}
counter = 0

while True:
    line = input()

    if "-" in line:
        name, number = line.split("-")
        phonebook[name] = number

    if line.isdigit():
        counter = int(line)
        break

for _ in range(0, counter):
    person = input()

    if person in phonebook.keys():
        print(f"{person} -> {phonebook[person]}")
    else:
        print(f"Contact {person} does not exist.")