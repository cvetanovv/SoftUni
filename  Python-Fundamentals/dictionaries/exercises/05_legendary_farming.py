key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
break_command = False
while not break_command:
    command = input().split()
    for i in range(0, len(command), 2):
        material = command[i + 1].lower()
        quantity = int(command[i])
        if material in key_materials:
            key_materials[material] += quantity
        else:
            if material not in junk_materials:
                junk_materials[material] = quantity
            else:
                junk_materials[material] += quantity
        if key_materials["shards"] >= 250:
            key_materials["shards"] -= 250
            print("Shadowmourne obtained!")
            break_command = True
        elif key_materials["fragments"] >= 250:
            key_materials["fragments"] -= 250
            print("Valanyr obtained!")
            break_command = True
        elif key_materials["motes"] >= 250:
            key_materials["motes"] -= 250
            print("Dragonwrath obtained!")
            break_command = True
        if break_command:
            break

sorted_key_materials = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for material, quantity in sorted_key_materials:
    print(f"{material}: {quantity}")

sorted_junk_materials = sorted(junk_materials.items(), key=lambda kvp: kvp[0])
for k, v in sorted_junk_materials:
    print(f"{k}: {v}")