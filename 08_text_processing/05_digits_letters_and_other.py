data = input()
digits = ""
letters = ""
characters = ""

for char in data:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        characters += char

print(digits)
print(letters)
print(characters)