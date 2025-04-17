people = int(input())
capacity = int(input())

counter = 0

for i in range(people):
    if people > 0:
        counter += 1
        people -= capacity

print(counter)