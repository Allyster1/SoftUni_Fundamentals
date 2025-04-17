import re

text = input()
pattern = r""

match = re.findall(pattern, text)
print(', '.join(match))
