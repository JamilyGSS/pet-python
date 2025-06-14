lista_compras = {}

def adicionar_item():
    novo_item = input('Digite o novo item: ')
    if novo_item in lista_compras:
        lista_compras[novo_item] += int(input(f'O item já existe. Quantidade adicional para {novo_item}: '))
    else:
        lista_compras[novo_item] = int(input(f'Digite a quantidade de {novo_item}: '))
    print()

def remover_item():
    if not lista_compras:
        print('O carrinho está vazio.\n')
        return
    item = input('Digite o item que você quer remover: ')
    if item in lista_compras:
        del lista_compras[item]
        print(f'{item} foi removido.\n')
    else:
        print('Item não encontrado no carrinho.\n')

def atualizar_lista():
    if not lista_compras:
        print('O carrinho está vazio.\n')
        return
    item = input('Digite o item que você deseja atualizar: ')
    if item in lista_compras:
        nova_quantidade = int(input(f'Nova quantidade para {item}: '))
        if nova_quantidade <= 0:
            del lista_compras[item]
            print(f'{item} foi removido.')
        else:
            lista_compras[item] = nova_quantidade
    else:
        print('Item não encontrado.\n')

def mostrar_lista():
    if not lista_compras:
        print('Carrinho vazio.\n')
        return
    print('\nItens no carrinho:')
    total_itens = 0
    for item, qtd in lista_compras.items():
        print(f'- {item}: {qtd}')
        total_itens += qtd
    print(f'Total de itens no carrinho: {total_itens}')

def limpar_carrinho():
    lista_compras.clear()
    print('Carrinho esvaziado!')

while True:
    print('O que você quer fazer?')
    print('[1] Adicionar item')
    print('[2] Remover item')
    print('[3] Atualizar quantidade')
    print('[4] Visualizar carrinho')
    print('[5] Limpar carrinho')
    print('[6] Sair')
    
    res = int(input('Digite sua opção: '))
    if res == 1:
        adicionar_item()
    elif res == 2:
        remover_item()
    elif res == 3:
        atualizar_lista()
    elif res == 4:
        mostrar_lista()
    elif res == 5:
        limpar_carrinho()
    elif res == 6:
        print('Saindo do programa. Até mais!')
        break
    else:
        print('Opção inválida! Tente novamente.\n')
