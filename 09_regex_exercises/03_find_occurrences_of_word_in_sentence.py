import re

text = input().lower()
word = input().lower()

pattern = f"{word}\\b"

matches = re.findall(pattern, text)
print(matches.count(word))