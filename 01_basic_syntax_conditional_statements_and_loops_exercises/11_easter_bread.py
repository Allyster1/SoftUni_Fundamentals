budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_per_loaf = milk_price_per_liter * 0.25
cost_per_loaf = flour_price + egg_price + milk_per_loaf

loaves = 0
colored_eggs = 0
remaining_budget = budget

while remaining_budget >= cost_per_loaf:
    loaves += 1
    remaining_budget -= cost_per_loaf
    colored_eggs += 3
    if loaves % 3 == 0:
        eggs_lost = loaves - 2
        colored_eggs -= eggs_lost

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left.")