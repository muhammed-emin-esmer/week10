import random

fileHeroes = "heroes.txt"
fileVillains = "villains.txt"
fileWeapons = "weapons.txt"

startHealth = 100


def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
    return random.choice(data).strip()


def attack(attacker, weapon, defender, defenderHealth):
    damage = len(weapon)
    defenderHealth = defenderHealth - damage
    if defenderHealth < 0:
        defenderHealth = 0

    print(attacker, "attacks", defender, "with the", weapon + "!")
    print("  Damage:", damage)
    print(" ", defender, "has", defenderHealth, "health left")
    return defenderHealth


randomHero = load_data(fileHeroes)
randomVillain = load_data(fileVillains)

heroWeapon = load_data(fileWeapons)
villainWeapon = load_data(fileWeapons)

# Weapon Randomizer
while villainWeapon == heroWeapon:
    villainWeapon = load_data(fileWeapons)

heroHealth = startHealth
villainHealth = startHealth

print("=== EPIC FIGHT ===")
print("Hero:", randomHero, "| Weapon:", heroWeapon, "| Damage:", len(heroWeapon))
print("Villain:", randomVillain, "| Weapon:", villainWeapon, "| Damage:", len(villainWeapon))
print()

roundNumber = 1
while heroHealth > 0 and villainHealth > 0:
    print("--- Round", roundNumber, "---")

    villainHealth = attack(randomHero, heroWeapon, randomVillain, villainHealth)
    if villainHealth == 0:
        break

    heroHealth = attack(randomVillain, villainWeapon, randomHero, heroHealth)

    print()
    roundNumber = roundNumber + 1

print()
print("=== GAME OVER ===")
if heroHealth > 0:
    print(randomHero, "wins with the", heroWeapon + "!")
else:
    print(randomVillain, "wins with the", villainWeapon + "!")