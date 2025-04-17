pattern = int(input())

for i in range(1, pattern + 1):
    print(i * "*")

for k in range(pattern - 1, -1, -1):
    print(k * "*")