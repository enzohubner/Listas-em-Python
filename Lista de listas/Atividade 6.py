numero = [1, 1, 2, 4, 5, 4, 7]
reserva = []

for n in numero:
    if n not in reserva:
        reserva.append(n)
print(reserva)        