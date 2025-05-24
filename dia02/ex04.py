lista = [0,10,5,50,1]
maior = lista[0]
for n in lista:
    if n > maior:
        maior = n
print(f'O maior número da lista {lista} é {maior}')