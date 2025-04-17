n = int(input())
flag = False

for _ in range(n):
    current = int(input())

    if current % 2 != 0:
        print(f"{current} is odd!")
        flag = False
        break
    flag = True

if flag == True:
    print("All numbers are even.")