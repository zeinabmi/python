sukupuoli = input("Anna biologinen sukupuoli:")
hb = int(input("Anna hemoglobiiniarvo:(g/1):"))
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")