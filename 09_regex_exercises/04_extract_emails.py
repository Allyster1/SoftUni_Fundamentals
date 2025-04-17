import re
text = input()

pattern = r"\b(?<![-._])(?!.*[-._]{2})[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,63}@(?!-)[a-zA-Z0-9-]{1,63}(?:\.[a-zA-Z0-9-]{1,63})+\b"
matches = re.findall(pattern, text)

print('\n'.join(matches))