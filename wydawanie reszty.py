kwota = int(input("Wpisz wartość: "))
nominal = [50, 20, 10, 5, 2, 1]
wartosc = 0

for x in nominal:
    wartosc = wartosc + kwota // x
    kwota = kwota % x
    print(x, kwota // x)