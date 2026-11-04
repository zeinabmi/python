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


hissi = Hissi(1, 10)

hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)