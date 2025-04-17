import re

text = []
while True:
    line = input().strip()
    if line == "":
        break
    text.append(line)

pattern = r"\d+"
matches = re.findall(pattern, '\n'.join(text))
print(' '.join(matches))
