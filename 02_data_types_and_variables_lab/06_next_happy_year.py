year = int(input())

while True:
    year += 1
    new_year = str(year)
    set_year = set(new_year)

    if len(new_year) == len(set_year):
        break


print(year)