legendary_obtained = False

legendary_items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

junk_items = {}

while legendary_obtained is False:
    input_materials = input().split()

    for i in range(0, len(input_materials), 2):
        quantity = int(input_materials[i])
        material = input_materials[i + 1].lower()

        if material == "shards":
            legendary_items["shards"] += quantity
            if legendary_items["shards"] >= 250:
                legendary_items["shards"] -= 250
                print("Shadowmourne obtained!")
                legendary_obtained = True
                break
        elif material == "fragments":
            legendary_items["fragments"] += quantity
            if legendary_items["fragments"] >= 250:
                legendary_items["fragments"] -= 250
                print("Valanyr obtained!")
                legendary_obtained = True
                break
        elif material == "motes":
            legendary_items["motes"] += quantity
            if legendary_items["motes"] >= 250:
                legendary_items["motes"] -= 250
                print("Dragonwrath obtained!")
                legendary_obtained = True
                break

        if material not in ["shards", "motes", "fragments"] and material not in junk_items:
            junk_items[material] = quantity
        elif material not in ["shards", "motes", "fragments"] and material in junk_items:
            junk_items[material] += quantity

for material, quantity in legendary_items.items():
    print(f"{material}: {quantity}")

for material, quantity in junk_items.items():
    print(f"{material}: {quantity}")