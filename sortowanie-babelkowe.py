lista = [10, 7, 8, 3, 2, 11]

for x in lista:
    print(x, end=' ')
print('')

for i in range(len(lista)):
    for j in range (len(lista) - 1 - i):
        if lista [j] > lista [j+1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp
    for x in lista:
        print(x,end=', ')
    print('')