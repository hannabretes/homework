operacja = input("Podaj operację jaką chcesz wykonać: + dodawanie, - odejmowanie, * mnożenie, / dzielenie: ")

x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))
wynik = int(0)

if operacja == "+":
    wynik = x+y
elif operacja == "-":
    wynik = x-y
elif operacja == "*":
    wynik = x * y
elif operacja == "/":
    wynik = x/y
else:
    wynik = "niepoprawne działanie"
print(wynik)