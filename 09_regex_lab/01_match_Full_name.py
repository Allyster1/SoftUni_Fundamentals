import re

names = input()
pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

match = re.findall(pattern, names)
print(' '.join(match))