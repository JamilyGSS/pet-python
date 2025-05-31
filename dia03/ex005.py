multiplicador = 2
def multiplica(num: float) -> float:
        '''Retorna o produto do *num* pelo multiplicador.
        Exemplos:
        >>> multiplica(1.5)
        3.0
        >>> multiplica(-1)
        -2
        '''
        return num*multiplicador

print(multiplica(-2.5))