class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.nopeus * tunnit


auto = Auto("ABC-123", 142)
auto.nopeus = 60
auto.kuljettu_matka = 2000
auto.kulje(1.5)

print(auto.kuljettu_matka)