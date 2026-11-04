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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


# Pääohjelma

sahkoauto = Sähköauto("ABC-15", 180, 52.5)

polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.nopeus = 100
polttomoottoriauto.nopeus = 120

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print("Sähköauton matkamittari:", sahkoauto.kuljettu_matka, "km")
print("Polttomoottoriauton matkamittari:",
      polttomoottoriauto.kuljettu_matka, "km")