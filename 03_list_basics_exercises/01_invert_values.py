numbers_list = input().split(" ")
inverted_list = []

for current_num in numbers_list:
    num = int(current_num)
    if num > 0:
        inverted_list.append(-abs(num))
    else:
        inverted_list.append(abs(num))

print(inverted_list)