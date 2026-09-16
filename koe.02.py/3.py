nimi = input("Anna sinun nimi: ")
luku = int(input("Anna luku: "))
hinta = float(input("Mikä on kahvin hinta?"))
yhteensa = hinta * luku 
print(f"Hei {nimi}, kahvin hinta on {hinta} euroa. {luku} kahvia maksaa yhteensä {yhteensa} euroa.")
ylijaama  = yhteensa % 2
print(f"Ylijäämä on {ylijaama} euroa.")
