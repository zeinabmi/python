
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


autot = []

for i in range(1, 11):
    nopeus = random.randint(100, 200)
    auto = Auto("ABC-" + str(i), nopeus)
    autot.append(auto)

while True:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            break
    else:
        continue
    break

print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")
for auto in autot:
    print(auto.rekisteritunnus, auto.huippunopeus,
          auto.nopeus, auto.kuljettu_matka)
