numero = [1, 2, 4, 5, 2, 3, 4, 7]

for i in numero:
    if numero[i] % 2 == 0:
        numero[i] = 0

print(numero)