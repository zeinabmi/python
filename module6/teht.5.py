def karsi_parittomat(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)

    return uusi_lista


luvut = [1, 2, 3, 4, 5, 6, 7, 8]

uusi_lista = karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", uusi_lista)