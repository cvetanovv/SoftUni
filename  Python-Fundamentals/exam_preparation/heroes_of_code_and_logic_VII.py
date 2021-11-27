number_of_heroes = int(input())

heroes = {}
for _ in range(number_of_heroes):
    build_hero = input().split()
    name = build_hero[0]
    hp = int(build_hero[1])
    mana = int(build_hero[2])
    heroes[name] = {"hp": hp, "mana": mana}

command = input()

while command != "End":
    command = command.split(" - ")
    ability = command[0]
    if ability == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]["mana"] >= mp_needed:
            heroes[hero_name]["mana"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif ability == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = (command[3])
        if heroes[hero_name]["hp"] - damage <= 0:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["hp"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    elif ability == "Recharge":
        hero_name = command[1]
        amount_mp = int(command[2])
        if heroes[hero_name]['mana'] + amount_mp > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['mana']} MP!")
            heroes[hero_name]['mana'] = 200
        else:
            heroes[hero_name]['mana'] += amount_mp
            print(f"{hero_name} recharged for {amount_mp} MP!")
    elif ability == "Heal":
        hero_name = command[1]
        amount_hp = int(command[2])
        if heroes[hero_name]['hp'] + amount_hp > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['hp']} HP!")
            heroes[hero_name]['hp'] = 100
        else:
            heroes[hero_name]['hp'] += amount_hp
            print(f"{hero_name} healed for {amount_hp} HP!")
    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hp"], kvp[0]))

for hero_n, hp_mana in sorted_heroes:
    print(hero_n)
    print(f"  HP: {heroes[hero_n]['hp']}")
    print(f"  MP: {heroes[hero_n]['mana']}")