"""
Napisz program który stworzy słownik gdzie kluczem będzie kolejna liczba z przedziału <0, 10>
a wartością ta liczba podniesiona do kwadratu
np: {0: 0, 1: 1, 2: 4, 3: 9, [...]}
"""



slownik = {}
range(0, 11)
for r in range(0,11):
    slownik[r] = r**2
print(slownik)