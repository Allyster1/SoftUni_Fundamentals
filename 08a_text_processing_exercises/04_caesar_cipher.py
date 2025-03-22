text = input()
encrypted_text = ""

for i in range(len(text)):
    encryption = ord(text[i]) + 3
    encrypted_text += chr(encryption)

print(encrypted_text)

