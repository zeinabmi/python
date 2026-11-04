class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()

        while self.kerros > kohde:
            self.kerros_alas()

    def kerros_ylös(self):
        self.kerros += 1
        print("Hissi on kerroksessa", self.kerros)

    def kerros_alas(self):
        self.kerros -= 1
        print("Hissi on kerroksessa", self.kerros)


class Talo:
    def __init__(self, alin, ylin, hissien_lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohde):
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohde)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 4)

talo.palohalytys()