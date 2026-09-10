def muunna_litroiksi(gallona):
    return gallona * 3.785


while True:
    gallona = float(input("Anna gallonamäärä: "))

    if gallona < 0:
        break

    litrat = muunna_litroiksi(gallona)
    print("Litroina:", litrat)