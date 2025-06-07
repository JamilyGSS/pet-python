def loja(lista:list[str]) -> int:
    '''Retorna a quantidade total de clientes únicos a partir da *lista*.
    Exemplos:
    >>> loja(['Ana','Ana','Vitor','Ana','Vitor','Lili'])
    3
    >>> loja(['Juju','Gigi','Lili','Shishi'])
    4
    >>> loja(['Gigi','Juju','Gigi','Juju'])
    2
    '''
    set_unico = set(lista)
    return len(set_unico)