first = input()
second = input()
last_printed = first

for char in range(len(first)):
    left = second[:char + 1]
    right = first[char + 1:]
    new_string = left + right

    if new_string != last_printed:
        print(new_string)
        last_printed = new_string