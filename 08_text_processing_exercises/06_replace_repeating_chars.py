letters_sequence = input()
result = ""
current_letter = ""

for letter in letters_sequence:
    if current_letter == "" or current_letter != letter:
        current_letter = letter
        result += letter

print(result)
