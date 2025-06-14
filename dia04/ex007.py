lista_compras = {}

def verificar_res(num: int) -> int:
    if num != 1 and num != 2 and num != 3 and num != 4 and num != 5:
        print('Resposta Inválida! Tente novamente!\n')
        return 0
    return num

def adicionar_item(lista1: dict) -> dict:
    novo_item = input('Digite o novo item: ')
    teste = True
    while teste:
        if novo_item in lista_compras:
            print('O item já está na lista! Tente novamente!')
            novo_item = input('Digite o novo item: ')
        else:
            teste = False
    quant_novo_item = int(input(f'Digite a quantidade de {novo_item} desejada: '))
    print()
    lista_compras[novo_item] = quant_novo_item
    return lista_compras

def remover_item(lista1: dict) -> dict:
    item_excluido = input('Digite o item que você quer excluir: ')
    teste = True
    while teste:
        if item_excluido not in lista_compras:
            print('O item não está na lista! Tente novamente!')
            item_excluido = input('Digite o item que você quer excluir: ')
        else:
            teste = False
    print()
    del lista_compras[item_excluido]
    return lista_compras

def atualizar_lista(lista1: dict) -> dict:
    print(lista_compras)
    item_atualizado = input('Digite o item que você deseja atualizar a quantidade: ')
    teste = True
    while teste:
        if item_atualizado not in lista_compras:
            print('O item não está na lista! Tente novamente!')
            item_atualizado = input('Digite o item que você deseja atualizar a quantidade: ')
        else:
            teste = False
    print()
    quant_nova = int(input(f'Digite a nova quantidade para {item_atualizado}: '))
    if quant_nova <= 0:
        del lista_compras[item_atualizado]
    else:
        lista_compras[item_atualizado] = quant_nova
    return lista_compras

def mostrar_lista(lista1: dict) -> None:
    if not lista1:
        print('Carrinho vazio!\n')
    else:
        for item, quantidade in lista1.items():
            print(f'{item}: {quantidade}')
        print()

res = 0
while res != 5:
    res = int(input(
        'O que você quer fazer? \n[1] Adicionar Novo Item \n[2] Remover um Item \n[3] Atualizar a Quantidade de um Item \n[4] Visualizar a lista \n[5] Sair do Programa \n'
    ))
    res = verificar_res(res)
    if res == 1:
        adicionar_item(lista_compras)
    elif res == 2:
        remover_item(lista_compras)
    elif res == 3:
        atualizar_lista(lista_compras)
    elif res == 4:
        mostrar_lista(lista_compras)
