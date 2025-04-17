import re

completed = False
valid_links = []
pattern = r"\b(?:www\.)(?:[a-zA-Z0-9-]+)(?:\.[a-z]+)+\b"

while completed is False:
    line = input()

    if line == "":
        completed = True
        break

    match = re.findall(pattern, line)
    if match:
        valid_links.append(match)

for link in valid_links:
    print(''.join(link))
