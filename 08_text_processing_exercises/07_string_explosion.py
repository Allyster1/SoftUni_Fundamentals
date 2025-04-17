text = input()
result = ""

counter = 0

for i in range(len(text)):
    if counter > 0 and text[i] != ">":
        counter -= 1
    elif text[i] == ">":
        result += ">"
        counter += int(text[i + 1])
    else:
        result += text[i]

print(result)