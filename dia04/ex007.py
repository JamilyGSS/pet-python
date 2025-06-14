lista_compras = {}

def verificar_res(num: int) -> int:
    if num != 1 and num != 2 and num != 3 and num != 4 and num != 5:
        print('Resposta Inválida! Tente novamente!')
        print()
    res = 0
    return res

def adicionar_item(lista1: list) -> list:
    novo_item = input('Digite o novo item: ')
    teste = True
    while teste:
        if novo_item in lista_compras:
            print('O item já está na lista! Tente novamente!')
            novo_item = input('Digite o novo item: ')
        else:
            teste = False
    quant_novo_item: int = int(input(f'Digite a quantidade de {novo_item} desejada: '))
    print()
    lista_compras[novo_item] = quant_novo_item
    return lista_compras

def remover_item(lista1: list) -> list:
    item_excluido = input('Digite o item que você quer excluir: ')
    teste = True
    while teste:
        if item_excluido not in lista_compras:
            print('O item não está na lista! Tente novamente!')
            item_excluido = input('Digite o novo item: ')
        else:
            teste = False
    print()
    lista_compras.remove(item_excluido)
    return lista_compras

res = 0
while res != 5:
    res = int(input('O que você quer fazer? \n[1] Adicionar Novo Item \n[2] Remover um Item \n[3] Atualizar a Quantidade de um Item \n[4] Visualizar a lista \n[5] Sair do Programa \n'))
    verificar_res(res)
    if res == 1:
        adicionar_item(lista_compras)
    elif res == 2:
        remover_item(lista_compras)
