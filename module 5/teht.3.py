luku = int(input(" Anna kokonaisluku: "))
alkuluku = True
if luku < 2:
    alkuluku = False
else:
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break
if alkuluku:
    print(luku, "on alkuluku.")
else:
    print(luku, "ei ole alkuluku.")
    