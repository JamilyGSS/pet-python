valores = [2,-3,0,5,6,7,8,1,106,-4]
pares = []
impares = []
for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista: {valores}')
print(f"Números pares: {pares}")
print(f'Números ímpares: {impares}')