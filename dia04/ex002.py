notas = {'Leandro': [0.2,4.6,9], 'Bernardo':[4.9,8,4.7] , 'Lucas':[7,8.9,2]}

for nome, media in notas.items():
    print(f'Média de {nome}: {sum(notas[nome])/3:.2f}')
    if sum(notas[nome])/3 < 6:
        print('Aluno REPROVADO')
    else:
        print('Aluno APROVADO')