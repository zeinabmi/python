import random
maara = int(input("Montako noppa heitetään?"))
summa = 0
for i in range(maara):
    silmaluku = random.randint(1, 6)
    summa += silmaluku
    print("Silmälukujen summa on:", summa)