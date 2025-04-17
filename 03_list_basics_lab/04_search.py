n = int(input())
word = input()

str_list = []

for _ in range(n):
    current_str = input()
    str_list.append(current_str)

print(str_list)

for i in range(len(str_list) -1, -1, -1):
    el = str_list[i]
    if word not in el:
        str_list.remove(el)
print(str_list)