"""
Napisz program który będzie prostą bazą danych w pamięci.
Program powinien pozwolić na:
 - wczytanie danych osoby,
 - wypisanie wczytanych osób,
 - wyszukanie osoby lub osób po wybranym polu i jego wartości
Program powinien działać do momentu wprowadzenia komendy końca
"""

komenda = "start"
bazaDanych = {}
while komenda != "koniec'":
    x = int(input(" [1] Wczytaj dane: \n [2] Wypisz dane: \n [3] Wyszukaj dane: \n [4] Koniec: \n"))
    print(x)
    if x == 1:
        daneOsoby = {}
        indeks = input("Podaj indeks - musi byc unikatowy")
        imie = input("Podaj imię: ")
        daneOsoby["imię"] = imie
        nazwisko = input("Podaj nazwisko: ")
        daneOsoby["nazwisko"] = nazwisko
        wiek = input("Podaj wiek: ")
        daneOsoby["wiek"] = wiek
        komenda = "dalej"
        bazaDanych[indeks] = daneOsoby
    elif x == 2:
        print(bazaDanych)
        komenda = 'dalej'
    elif x == 3:
        klucz = int(input("Po jakim kluczu chcesz wyszukać? \n [1] imię: \n [2] nazwisko: \n [3] wiek: \n"))
        szukana = input("Wpisz wartość do wyszukania: ")
        if klucz == 1:
            for i,j in bazaDanych.items():
                for k in j:
                    if k == "imie" and j[k] == szukana:
                        print(j)
        elif klucz == 2:
            for i,j in bazaDanych.items():
                for k in j:
                    if k == "nazwisko" and j[k] == szukana:
                        print(j)
        elif klucz == 3:
            for i,j in bazaDanych.items():
                for k in j:
                    if k == "wiek" and j[k] == szukana:
                        print(j)
        else:
            print("Błędna wartość!")
            komenda = "dalej"
    elif x == 4:
        break
        # komenda = "koniec"
    else:
        print("Błędna wartość!")
