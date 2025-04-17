factor = int(input())
count = int(input())

num_list = []

for i in range(1, count + 1):
    i *= factor
    num_list.append(i)

print(num_list)