letters_list = input()

sorted_letters = [letter for letter in letters_list if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(sorted_letters))