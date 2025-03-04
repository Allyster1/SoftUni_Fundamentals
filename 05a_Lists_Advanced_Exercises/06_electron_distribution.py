number_of_electrons = int(input())
shells = []

for current_shell in range(1, number_of_electrons + 1):
    max_electrons = 2 * current_shell ** 2
    if number_of_electrons > max_electrons:
        shells.append(max_electrons)
        number_of_electrons -= max_electrons
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)