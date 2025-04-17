characters_list = input().split()
char_dict = {}

for char in characters_list:
    for occurrences in char:
        if occurrences not in char_dict:
            char_dict[occurrences] = 1
        else:
            char_dict[occurrences] += 1

for char, occurrences in char_dict.items():
    print(f"{char} -> {occurrences}")