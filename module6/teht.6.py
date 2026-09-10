import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    pinta_ala_m2 = pinta_ala / 10000
    return hinta / pinta_ala_m2


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))

hinta_m2_1 = yksikkohinta(halkaisija1, hinta1)
hinta_m2_2 = yksikkohinta(halkaisija2, hinta2)

if hinta_m2_1 < hinta_m2_2:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
elif hinta_m2_2 < hinta_m2_1:
    print("Toinen pizza on parempi vastine rahalle.")
else:
    print("Pizzat ovat yhtä hyviä vastineita rahalle.")