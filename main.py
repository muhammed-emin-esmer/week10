import random

fileHeroes = "heroes.txt"
fileVillains = "villains.txt"

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
    return random.choice(data).strip()

randomHero = load_data(fileHeroes)
randomVillain = load_data(fileVillains)

print(randomHero)
print(randomVillain)