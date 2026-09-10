lentoasemat = {}

while True:
    toiminto = input("Haluatko syöttää uuden lentoaseman, hakea lentoaseman tai lopettaa? ")

    if toiminto == "syöttää":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif toiminto == "hakea":
        icao = input("Anna ICAO-koodi: ")

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "lopettaa":
        break