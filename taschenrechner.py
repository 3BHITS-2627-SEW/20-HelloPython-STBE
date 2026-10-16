zahl1 = int(input("Erste Zahl:"))
zahl2 = int(input("Zweite zahl:"))
ergebnis = zahl1 + zahl2
print("Ergebnis: ", ergebnis)

modulo = ergebnis % 2 
if modulo == 1:
    print("Ergebnis ist ungerade")
if modulo == 0:
    print("Ergebnis ist gerade")

