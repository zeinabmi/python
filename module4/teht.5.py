tunnus = "python"
salasana = "rules"

yritykset = 0

while yritykset < 5:
    kayttajatunnus = input("Käyttäjätunnus: ")
    kayttajasalasana = input("Salasana: ")

    if kayttajatunnus == tunnus and kayttajasalasana == salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")
    