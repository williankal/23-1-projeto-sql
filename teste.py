lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range (len(lista)):
    if lista[i] == 2:
        print(lista[i])
        lista.pop(lista[i])

print(lista)
        