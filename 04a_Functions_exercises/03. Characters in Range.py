def char_in_ascii(first: str, second: str) -> list:
    ascii_data = []

    ascii_char1 = ord(first)
    ascii_char2 = ord(second)
    for i in range(ascii_char1 + 1, ascii_char2):
        ascii_data.append(chr(i))

    return ascii_data


first_character = input()
second_character = input()

result = char_in_ascii(first_character, second_character)

print(" ".join(result))