leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))
luodit = leiviska * 20 * 32 + naula * 32 + luoti
grammat = luodit * 13.3
kilot = int(grammat // 1000)
grammat = int(grammat % 1000)
print("Massaon", kilot,"kg ja", grammat ,"g.")