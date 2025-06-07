notas = {'Leandro': [0.2,4.6,9], 'Bernardo':[4.9,8,4.7] , 'Lucas':[7,8.9,2]}

for nome, notas in notas.items():
    media = sum(notas)/3
    print(f'Média de {nome}: {media:.2f}')
    if media < 6:
        print('Aluno REPROVADO')
    else:
        print('Aluno APROVADO')