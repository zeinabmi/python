import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos,
                                 self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print()
        print(self.nimi)
        print("-" * 60)
        print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")

        for auto in self.autot:
            print(auto.rekisteritunnus, auto.huippunopeus,
                  auto.nopeus, auto.kuljettu_matka)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True

        return False


autot = []

for i in range(1, 11):
    nopeus = random.randint(100, 200)
    auto = Auto("ABC-" + str(i), nopeus)
    autot.append(auto)


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()

print("Kilpailu on päättynyt!")