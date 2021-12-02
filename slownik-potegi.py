"""
Napisz program który stworzy słownik gdzie kluczem będzie kolejna liczba z przedziału <0, 10>
a wartością ta liczba podniesiona do kwadratu
np: {0: 0, 1: 1, 2: 4, 3: 9, [...]}
"""

some_dict = {}

range(11)
for r in range(11):
    some_dict[r] = r ** 2
print(some_dict)
