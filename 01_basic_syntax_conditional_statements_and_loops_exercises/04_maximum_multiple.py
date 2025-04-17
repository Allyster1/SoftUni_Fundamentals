divisor = int(input())
boundaries = int(input())
n = 0

for i in range(0, boundaries + 1):
    if i / divisor > 0 and (i <= boundaries and i % divisor == 0):
        n = i

print(n)