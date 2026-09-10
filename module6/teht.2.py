import random

def noppa(tahkot):
    return random.randint(1, tahkot)

maksimi = int(input("Anna nopan maksimisilmäluku: "))

silmaluku = 0

while silmaluku != maksimi:
    silmaluku = noppa(maksimi)
    print(silmaluku)